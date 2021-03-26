#!/usr/bin/python2.7

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation
from rover_msgs.msg import JointState
import math
import time


jointEffort = 5 #joint effort for holding position in Nm
jointArray = list() #a global array of joints and associatated information about them. See JointState.msg for exact data

_client = Client() #ambf client innit.
_client.connect()
print("Got Here")

#takes message from control.py
#returns joint positions & confirmation


#just drag the tip and let the rest of the model follow along.
#add checks to make sure the tip doesnt get out of bounds.

class ArmControl(Client):
    JointInfo = JointState()
    def __init__(self,body, idx = -1, name = "undef"):
        #creates object for joint position
        if idx == -1:
            rospy.logwarn("No IDX provided. Joint control will not be possible Body movement only!")
        try:
            self.obj = _client.get_obj_handle(body)
            rospy.loginfo("Got-Object-Handle")
        except: 
            rospy.logwarn("An Error occured while creating joint!")
            raise
        else:
            rospy.loginfo("Body: " + str(self) + " connected to: " + str(body) + "at idx =" + str(idx))

        constJointState = JointState()
        #adding joint to constJointArray list
        if name == "undef":
            constJointState.name = str(body) + "-joint::" + str(idx)
        else:
            constJointState.name = name

        constJointState.idx = idx
        constJointState.parentName = body
        jointArray.append(constJointState) #adds jointstate to array to allow for mass manipulation in Unified Control

        self.JointInfo = constJointState


    def Move(self,POS,RPY):
        if type(POS) != 'list' or type(RPY) != 'list':
            #makes sure the right data-type is supplied
            pass
            #raise TypeError("Expected a list with 3 values, recieved: \n POS: " + str(type(POS)) + "\n RPY: " + str(type(RPY)))

        #Adds new pos/rpy to current versions

        #converts ambf point message type to a regular list.
        PointPos = self.obj.get_pos()
        pos = [
            PointPos.x,
            PointPos.y,
            PointPos.z   
        ]

        pos = pos + POS
        rot = list(self.obj.get_rpy()) + RPY
        #execute
        self.obj.set_pos(pos[0],pos[1],pos[2])
        print("POS:" + str(POS))
        self.obj.set_rpy(rot[0],rot[1],rot[2])
        print("ROT:" + str(RPY))
        #return
        rospy.sleep(0.2)

    def ABSmove(self,POS,RPY):
        if type(POS) != 'list' or type(RPY) != 'list':
            #makes sure the right data-type is supplied
            raise TypeError("Expected a list with 3 values, recieved: \n POS: " + str(type(POS)) + "\n RPY: " + str(type(RPY)))
            
        self.obj.set_pos(POS[0],POS[1],POS[2])
        self.obj.set_rpy(ROT[0],ROT[1],ROT[2])
        return

    def holdPOS(self, Effort):
        if not self.JointInfo.idx == -1:
            #print(self.JointInfo)
            self.obj.set_joint_effort(self.JointInfo.idx, Effort) #joint index errors coming from here.
        
    

class UnifiedControl(Client):
    #[[JointName,Idx,Torque],[JointName,Idx,Torque]...]
    #def __init__(self):
    #    pass

    @staticmethod
    def uniHoldPOS(hold = True):
        #allows joints to hold position even when moving
        if not hold:
            modjointEffort = 0
        else:
            modjointEffort = jointEffort

        for i in range(0, len(Joints)- 2):
            #loops through jointArray to set the torque/effort for joints to a previosly defined number skips last two objects since they are not joints.
            Joints[i].holdPOS(modjointEffort)

class ControllerMove(Client,UnifiedControl):
    #instead of moving entire arm. Only the wrist is moved and downstream joints are simply left to comply.
    global Joints
    def __innit__(joints):
        #takes the joints and internalizes it
        #self.Joints = joints
        #self.UniJoint = UnifiedControl()
        pass

    def WristMove(self):
        #computes the position of the wrist based on controller inputs
        Dpos = [0,0,0,0]#XYZ + rot
        Roll = [0,0,0]

        if Controller.axes[7] != 0:
            Dpos[1] = Controller.axes[7]
            #Y-axis
        if Controller.axes[6] != 0:
            Dpos[0] = Controller.axes[6]
            #X-axis
        if Controller.buttons[4] or Controller.buttons[5]:
            Roll[0] = (Controller.buttons[5] + (-1 * Controller.buttons[4]))/36
            #shoulder buttons :: rotate wrist
        if Controller.axes[2] or Controller.axes[5] != -1:
            #triggers for Z
            #+1  / 2 
            Dz = (((Controller.axes[2]) + 1 /2) + ((Controller.axes[5]) +1 / -2))
            Dpos[2] = Dz
        
        self.uniHoldPOS(False) #disables torque on joints
        Joints[4].Move(Dpos,Roll) 
        # print(Joints[4])
        self.uniHoldPOS(True) #re-enables torque on joints




#Create body class constructer
def CreateJoints():
    #needs to return to make sure this remains in the scope of main()
    jointreturn = [
    ArmControl("RoverBody",4,"Shoulder"),
    ArmControl("Shoulder",0,"UpperArm"),
    ArmControl("UpperArm",0,"ForeArm"),
    ArmControl("ForeArm",0,"Wrist"),
    ArmControl("Wrist",-1,"Hand"),
    _client.get_obj_handle('tip_sensor'),
    _client.get_obj_handle('tip_actuator0')]

    return jointreturn

Joints = CreateJoints()


class Joystick:
    def __init__(self):
        print("Joystick class init")
    axes = [0] * 8 #creates an empty list with all 0 since otherwise when first starting sometimes the script will fail when trying to access and out of index number
    buttons =[0] * 11 

Controller = Joystick()
def Joystick_CB(data):
    #rounds joystick inputs to 3 digits to prevent micromovents
    for i in range(0,len(data.axes)):
        Controller.axes[i] = round(data.axes[i],3)
    # Controller.axes = data.axes
    Controller.buttons = data.buttons




def main():
    #connects to client

    #Stiffens arm by default when starting to prevent it from flopping around.
    UnifiedControl.uniHoldPOS(True)

    rospy.Subscriber("joy",Joy,Joystick_CB)
    #Joints = CreateJoints()
    Arm = ControllerMove(Joints)

    while not rospy.is_shutdown():
        Arm.WristMove()
        rate.sleep()

if __name__ == '__main__':
    #rospy.init_node('ArmControl')
    rospy.loginfo("Rover Node Started")
    try:
        rate = rospy.Rate(rospy.get_param("/rate"))
    except:
        rospy.logwarn("\"/rate\" parameter not set, defaulting to 60hz")
        rate = rospy.Rate(0.1)

    main()