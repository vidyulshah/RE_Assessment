#! /usr/bin/python3

import sys, time, copy, rospy, moveit_commander, moveit_msgs.msg, geometry_msgs.msg, actionlib, std_msgs

class six_axis_robot_arm():
    def __init__(self, Group_Name):
        rospy.init_node('axis_robot_arm_node', anonymous=True)
        self.command = moveit_commander.roscpp_initialize(sys.argv)
        self._robot = moveit_commander.RobotCommander()
        self._scene = moveit_commander.PlanningSceneInterface()
        self._planning_group = Group_Name
        self._group = moveit_commander.MoveGroupCommander(self._planning_group)
        self._display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
        self._exectute_trajectory_client = actionlib.SimpleActionClient('execute_trajectory', moveit_msgs.msg.ExecuteTrajectoryAction)
        self._exectute_trajectory_client.wait_for_server()
        self._planning_frame = self._group.get_planning_frame()
        self._eef_link = self._group.get_end_effector_link()
        self._group_names = self._robot.get_group_names()

        # Publisher for arm status
        self._arm_status_pub = rospy.Publisher('/arm_status', std_msgs.msg.String, queue_size=10)

    def set_pose(self, arg_pose_name):
        self._group.set_named_target(arg_pose_name)
        plan_success, plan, planning_time, error_code = self._group.plan()
        goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
        goal.trajectory = plan
        self._exectute_trajectory_client.send_goal(goal)
        self._exectute_trajectory_client.wait_for_result()

        # Publish status message
        if plan_success:
            self._arm_status_pub.publish("Position reached: {}".format(arg_pose_name))
        else:
            self._arm_status_pub.publish("Error setting pose: {}".format(arg_pose_name))

def main():
    arm = six_axis_robot_arm("arm_group")
    hand = six_axis_robot_arm("hand")
    rospy.sleep(5)
    arm.set_pose("straight_up")
    hand.set_pose("hand_closed")
    hand.set_pose("hand_opened")
    while not rospy.is_shutdown():
    	arm.set_pose("lift_object")
    	arm.set_pose("pick_up")
    	hand.set_pose("hand_closed")
    	arm.set_pose("object_translate")
    	arm.set_pose("drop_object")
    	hand.set_pose("hand_opened")

if __name__=='__main__':
    main()

