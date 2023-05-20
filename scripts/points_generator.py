#!/usr/bin/env python
import rospy
import random
from ar_week5_test.msg import cubic_traj_params


## What follows is a function to produce points for the graphs.
def points_generator():
## Here, I initialise my topics and nodes whilst setting the results rate (1/0.05Hz = 20 seconds) for my graph
    pub = rospy.Publisher('points', cubic_traj_params, queue_size=10)
    rospy.init_node('points_generator', anonymous=True)
    rate = rospy.Rate(0.05) 
    msg = cubic_traj_params()


## Now, I generate my random numbers for my parameters, which are published to the params.msg
    while not rospy.is_shutdown():
        msg.p0 = random.uniform(-10, 10)
        msg.pf = random.uniform(-10, 10)
        msg.v0 = random.uniform(-10, 10)
        msg.vf = random.uniform(-10, 10)
        msg.t0 = 0
        msg.tf = msg.t0 + round(random.uniform(5, 10), 0)
        rospy.loginfo(msg)
        pub.publish(msg)
        print(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:
        pass
