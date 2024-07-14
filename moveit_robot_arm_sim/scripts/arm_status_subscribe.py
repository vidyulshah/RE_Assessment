#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def arm_status_callback(msg):
    rospy.loginfo("Received arm status: %s", msg.data)

def arm_status_subscriber():
    rospy.init_node('arm_status_subscriber', anonymous=True)
    rospy.Subscriber("/arm_status", String, arm_status_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        arm_status_subscriber()
    except rospy.ROSInterruptException:
        pass

