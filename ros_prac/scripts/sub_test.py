#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

pose = Pose()

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y

def autonomous_controller():
    rospy.init_node('my_sub_test')
    sub = rospy.Subscriber('/turtle1/pose', Pose, update_pose)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo("x:%f,y:%f",pose.x,pose.y)
        rate.sleep()

if __name__ == '__main__':
    try:
        autonomous_controller()
    except rospy.ROSInterruptException:
        pass
