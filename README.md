Robotics Engineer - Assessment
Task - Basic Arm Movement with Status Reporting
Objective - Create a ROS package that controls a simple 6-DOF robotic arm ( any robotic arm design of your choice works, including open-source options) The package should enable the arm to move between predefined positions and report its status on a new topic.
Requirements:
1.	Initialize the Arm: Develop a node to initialize the robotic arm to its home position.
2.	Trajectory Execution: Implement a straightforward trajectory to guide the arm through a sequence of predefined positions.
3.	Status Reporting: Establish a new topic (e.g., /arm_status) to continuously update the arm's current status (e.g., "moving", "position reached", etc.).
4.	Bonus Task (Move to Position) - Implement a node utilizing joint space commands for precise arm positioning, integrating with MoveIt if applicable.
Packages/Language Used - Python3, Online Model of 6 axis robotic arm, Noetic Ninjemy's, Moveit_Commander, Moveit Assistant, rospy
Procedure - 
1.	git clone the following repo in your catkin_ws/src (your_workspace/src) folder
git clone https://github.com/vidyulshah/RE_Assessment.git (clone the master branch)
2.	cd catkin_ws
3.	catkin_make or catkin build (the first time you compiled your workspace)
4.	open new terminal and run roscore
5.	Then, in new terminal tab got to catkin_ws or your_workspace and source devel/setup.bash and then run, roslaunch moveit_robot_arm_sim full_robot_arm_sim use_rviz:=false
6.	Then in third terminal, source the bash script again and run, rosrun moveit_robot_arm_sim 1_robot_movement.py
7.	Then in other terminal tab, source the bash script and subscribe to the topic usign the script, rosrun moveit_robot_arm_sim arm_status_subscribe.py
Outcomes - The robot will get place in an empty world with all nodes of moveit commander running neccesary for robot topic, message and services. Then 1_robot_movement.py will start a node where the robot will move to straight_up position which is acting as a home position then close and open the robotic arm. Further, it will perform pick and place operation. This the whole process the status update will be given in /arm_status topic which can be accessed using arm_status_subscribe.py file, it will keep running endlessly until the file is closed.
Moveit_Setup Assistant Screenshots
 
 
 
 


