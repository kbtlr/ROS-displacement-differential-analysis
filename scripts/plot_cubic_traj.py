#!/usr/bin/env python
import rospy
from ar_week5_test.msg import cubic_traj_coeffs
from std_msgs.msg import Float64

def callback(data):    
## Here, I initialise my pubs, followed by my messages for each of the trajectories
    pub1 = rospy.Publisher('position', Float64, queue_size=10)
    pub2 = rospy.Publisher('velocity', Float64, queue_size=10)
    pub3 = rospy.Publisher('acceleration', Float64, queue_size=10)
    pos_traj = Float64()
    vel_traj = Float64()
    acc_traj = Float64()
## Initialise more variables for the loop
    freq = 100000
    v = (data.tf-data.t0) / freq
    tf = 0
## Now, the cubic formulae are implemented for each degree of derivation, followed by publishing the messages, in a loop
    for z in range(freq):
       tf += v
       pos_traj.data = data.a0 + (data.a1 * tf) + (data.a2 * (tf**2)) + (data.a3 * (tf**3))
       vel_traj.data = data.a1 + (2 * data.a2 * tf) + (3 * data.a3 * (tf**2))
       acc_traj.data = (2 * data.a2) + (6 * data.a3 * tf)
       pub1.publish(pos_traj)
       pub2.publish(vel_traj)
       pub3.publish(acc_traj)

def plot_cubic_traj():
## Now, I initialise a new node, subscribe to cubic_traj_params and then send any relevant data to callback. rospy.spin() prevents 
## the process from dying
    rospy.init_node('plot_cubic_traj', anonymous = True)
    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)
    rospy.spin()
if __name__ == "__main__":
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass

