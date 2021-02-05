from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation
import math
import time


_client = Client()
_client.connect()
Body = _client.get_obj_handle("RoverBody")

rate = rospy.Rate(1)

Body.set_pos(0,0,0)
Body.set_rpy(math.pi/2,0,0)
while not rospy.is_shutdown():
    #Body.set_pos(0,0,0)
    Body.set_rpy(math.pi/2,0,0)
    Body.set_pos(input(" in x: "),input(" in y: "),0)
    rospy.sleep(0.5)
    print(Body.get_pos())
    rate.sleep()