#!/usr/bin/python2.7

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation
from rover_msgs.msg import JointState
import math
import time


jointEffort = 5 #joint effort for holding position in Nm
jointArray = None

#takes message from control.py
#returns joint positions & confirmation


#just drag the tip and let the rest of the model follow along.
#add checks to make sure the tip doesnt get out of bounds.

class ArmControl(Client):
    obj = None
    constJointState = JointState()
    def __init__(self,body, idx = -1, name = "undef"):
        #creates object for joint position
        if idx == -1:
            rospy.logwarn("No IDX provided. Joint control will not be possible Body movement only!")
        try:
            self.obj = _client.get_obj_handle(body)
        except:
            raise 
            rospy.logwarn("An Error occured while creating joint!")
        else:
            rospy.loginfo("Body: " + str(self) + " connected to: " + str(body) + "at idx =" + str(idx))

            #adding joint to constJointArray list
            if name == "undef":
                constJointState.name() = str(body) + "-joint::" + str(idx)
            else:
                constJointState.name() = name

            constJointState.idx() = idx
            constJointState.parentName = body
            jointArray.append(constJointState) #adds jointstate to array to allow for mass manipulation in Unified Control
    def Move(self,POS,RPY):
        if type(POS) != 'list' or type(RPY) != 'list':
            raise TypeError("Expected a list with 3 values, recieved: \n POS: " + str(type(POS)) + "\n RPY: " + str(type(RPY)))
        
        #moves relativly
        rot = self.obj.get_rpy()
        pos = self.obj.get_pos()
        pos = Vector(round(pos.x,3),round(pos.y,3),round(pos.z,3))



    def ABSmove(self,POS,RPY)
        


    def holdPOS(self, hold):
        self.obj.set_joint_effort(jointidx, jointEffort)
    

class UnifiedControl(Client):
    #[[JointName,Idx,Torque],[JointName,Idx,Torque]...]
    def __init__():
        pass
    def uniHoldPOS(self, hold = True):
        #allows joints to hold position even when moving
        if not hold:
            modjointEffort = 0
        else:
            modjointEffort = jointEffort

        for i in jointArray:
            jointArray[i].name().set_joint_effort(jointArray[i].idx(),modjointEffort)
            jointArray.set



#Create body class constructer
def CreateJoints():
    #needs to return to make sure this remains in the scope of main()
    return [
    Shoulder.ArmControl("RoverBody",4,"Shoulder"),
    UpperArm.ArmControl("Shoulder",0,"UpperArm"),
    ForeArm.ArmControl("UpperArm",0,"ForeArm"),
    Wrist.ArmControl("ForeArm"0,"Wrist"),
    Hand.ArmControl("Wrist",0,"Hand"),
    sensor_array = _client.get_obj_handle(tip_sensor),
    gripper = _client.get_obj_handle(tip_actuator0)]

Controller = Joystick() #declared globally since a lot of things need access to it
def Joystick_CB(data):
    Controller.axes = data.axes
    Controller.buttons = data.buttons


def main():
    global _client
    _client = Client()
    _client.connect()

    rospy.Subscriber("joy",Joy,Joystick_CB)
    Joints = CreateJoints()
    


    while not rospy.is_shutdown():
        pass

if __name__ == '__main__':
    rospy.init_node('ArmControl')
    rospy.loginfo("Rover Node Started")
    rate = rospy.Rate(rospy.get_param("/rate"))
    main()