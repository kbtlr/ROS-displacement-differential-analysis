#!/usr/bin/env python
import rospy
from ar_week5_test.srv import *
from ar_week5_test.msg import cubic_traj_params
from ar_week5_test.msg import cubic_traj_coeffs

def callback(data):
## We start by initliasing publishing to the coeffs.msg
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size=0)

    try:
## Now, we connect to the cubic_traj service, to write new data back to it.
        compute = rospy.ServiceProxy('compute_service', compute_cubic_traj)
## The data received is then computed in to responses for our coefficients, and 
## finally published.
        resp = compute(data)
        msg = cubic_traj_coeffs()
        msg.a0 = resp.a0
        msg.a1 = resp.a1
        msg.a2 = resp.a2
        msg.a3 = resp.a3
        msg.t0 = data.t0
        msg.tf = data.tf
        print msg
        pub.publish(msg)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

## Now we initialise a new node named after the script, wait for our compute service,
## subscribe to cubic_traj_params.msg and finally send data to callback
def cubic_traj_planner():
    rospy.init_node('cubic_traj_planner', anonymous=True)
    rospy.wait_for_service('compute_service')
    rospy.Subscriber('points', cubic_traj_params, callback)
    rospy.spin()

if __name__ == "__main__":
    cubic_traj_planner()

