#!/usr/bin/python2.7

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation
from rover_msgs.msg import JointState
import math
import time


jointEffort = 5 #joint effort for holding position in Nm

#takes message from control.py
#returns joint positions & confirmation


#just drag the tip and let the rest of the model follow along.
#add checks to make sure the tip doesnt get out of bounds.

class ArmControl(Client):
    obj = None
    jointidx = None
    def __init__(self,body, idx):
        #creates object for joint position
        self.obj = _client.get_obj_handle(body)
        jointidx = idx
    def holdPOS(self, hold):
        self.obj.set_joint_effort(jointidx, jointEffort)
    

class UnifiedControl(ArmControl):
    jointArray = None
    #[[JointName,Idx,Torque],[JointName,Idx,Torque]...]
    def __init__(self, Array):
        jointArray = Array

    def uniHoldPOS(self, hold = True):
        #allows joints to hold position even when moving
        if not hold:
            modjointEffort = 0
        else:
            modjointEffort = jointEffort

        for i in jointArray:
            jointArray[i].name().set_joint_effort(jointArray[i].idx(),modjointEffort)





def main():
    global _client
    _client = Client()
    _client.connect()

    Arm.

    while not rospy.is_shutdown():
        pass

if __name__ == '__main__':
    rospy.init_node('ArmControl')
    rospy.loginfo("Rover Node Started")
    rate = rospy.Rate(rospy.get_param("/rate"))
    main()