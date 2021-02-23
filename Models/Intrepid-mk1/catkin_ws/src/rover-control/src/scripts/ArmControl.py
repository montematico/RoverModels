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
            #makes sure the right data-type is supplied
            raise TypeError("Expected a list with 3 values, recieved: \n POS: " + str(type(POS)) + "\n RPY: " + str(type(RPY))
            break
        #Adds new pos/rpy to current versions
        pos = self.obj.get_pos() + POS
        rot = self.obj.get_rpy() + RPY
        #execute
        self.obj.set_pos(pos[0],pos[1],pos[2])
        self.obj.set_rpy(rot[0],rot[1],rot[2])

    def ABSmove(self,POS,RPY):
        if type(POS) != 'list' or type(RPY) != 'list':
            #makes sure the right data-type is supplied
            raise TypeError("Expected a list with 3 values, recieved: \n POS: " + str(type(POS)) + "\n RPY: " + str(type(RPY))
            break
        self.obj.set_pos(POS[0],POS[1],POS[2])
        self.obj.set_rpy(ROT[0],ROT[1],ROT[2])


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

class ControllerMove(Client):
    Joints = None
    def __innit__(joints):
        #takes the joints and internalizes it
        Joints = joints
        UniJoint = UnifiedControl()
    def WristMove():
        if (Controller.Axes[6] or Controller.axes[7]) != 0 or (Controller.buttons[4] or Controller.buttons[5]) == 1:
            Delta_Z = Controller.buttons[4] + (-1 * Controller.buttons[5]) #Creates Z change. Pressing both nulls out the value and has a net-0 change.

            #2 LT, 5 RT 1    pi/36 = 10deg
            #theres like a %20 chance this math is right.
            Roll = (Controller.axes[2] * (math.pi /36)) - (Controller.axes[5] * (math.pi/36))

            UniJoint.uniHoldPOS(False) #releases joints  
            Joints[0].move([Controller.Axes[6],Controller.Axes[7],Delta_Z],[Roll,0,0])
            rospy.sleep(0.1)
            UniJoint.uniHoldPOS()

        else:
            UniJoint.uniHoldPOS()
            #if controller buttons not held simply hold previous position

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
    Arm = ControllerMove(Joints)

    while not rospy.is_shutdown():
        Arm.WristMove()

if __name__ == '__main__':
    rospy.init_node('ArmControl')
    rospy.loginfo("Rover Node Started")
    rate = rospy.Rate(rospy.get_param("/rate"))
    main()