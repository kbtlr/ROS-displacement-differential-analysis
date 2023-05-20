#!/usr/bin/env python
from ar_week5_test.srv import *
import rospy
import numpy 

## This function produces matrices from our params, and inverses the A matrix to yield our coefficients.
## These coefficients are returned to the msg.
def handle_compute_cubic_traj(req):
    params = req.params
    print 'Accepting Computation Request'
    A = numpy.matrix('1 %d %d %d; 0 1 %d %d; 1 %d %d %d; 0 1 %d %d' % (params.t0, params.t0**2, params.t0**3, 2*params.t0, 3*(params.t0**2), params.tf, params.tf**2, params.tf**3, 2*params.tf, 3*(params.tf**2)))
    C = numpy.matrix('%d %d %d %d' % (params.p0, params.v0, params.pf, params.vf))
    D = numpy.linalg.inv(A)
    B = C * D
    result = B.getA1().tolist()
    print 'Returning %s' % result
    return compute_cubic_trajResponse(result[0], result[1], result[2], result[3])

def compute_cubic_coeffs():
## As before, we initialise our node and service to allow our script to function.
    rospy.init_node('compute_cubic_coeffs')
    s = rospy.Service('compute_service', compute_cubic_traj, handle_compute_cubic_traj)
    
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeffs()

