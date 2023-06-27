#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

cmd_vel = Twist()
cmd_vel.linear.x = 2.0
cmd_vel.angular.z = 0.0

pose = Pose()
pose2 = Pose()

def update_pose2(data):
    global pose
    pose.x = data.x
    pose.y = data.y
    pose.theta = data.theta

def update_pose(data):
    global pose2
    pose2.x = data.x
    pose2.y = data.y
    pose2.theta = data.theta

def update_cmd_vel():
    global cmd_vel
    global nowRotating
    cmd_vel.linear.x = 0.5*abs(math.sqrt(((pose2.x-pose.x) ** 2) + ((pose2.y-pose.y)**2)))
    cmd_vel.angular.z =math.atan2(pose2.y-pose.y,pose2.x-pose.x)-pose.theta

def autonomous_controller():
    rospy.init_node('autonomous_controller')
    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, update_pose)
    sub2 = rospy.Subscriber('/turtle2/pose', Pose, update_pose2)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        update_cmd_vel()
        pub.publish(cmd_vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        autonomous_controller()
    except rospy.ROSInterruptException:
        pass
