#!/usr/bin/python2.7

#A script to allow for controlling of the rover using joystick inputs.
#will eventually be broken into several seperate scripts with topics and services to
# allow for easily switching control inputs or rover in and out 

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation
import math
import time

##################################################################
###################### JOYSTICK INPUT ############################
##################################################################
class Joystick:
    def __init__(self):
        print(" XB1 class init")
    axes = [0] * 8 #creates an empty list with all 0 since otherwise when first starting sometimes the script will fail when trying to access and out of index number
    buttons =[0] * 11 

Xb1 = Joystick()
def JoyInput(data):
    #rospy.loginfo(data.axes)
    Xb1.axes = data.axes
    Xb1.buttons = data.buttons
    #rospy.loginfo(data.buttons)
    #Axes are scaled to +-1
    #for i in range(0,len(data.axes)):
     #   axes[i] = data.axes[i]
    global joystick
    joystick = data
        



##################################################################
####################### Rover Control ############################
##################################################################

#creates an AMBF client and tries to connects to it

class Movement(Client):
    obj = None
    jointidx = 0
    def __init__(self, body):
        #constructor for movement object. Pass body name as string to connect.
        try:
            self.obj = _client.get_obj_handle(body)
        except:
            raise
            rospy.logwarn("An Error Occured while creating joint!")
        else:
            rospy.loginfo("Body: " + str(self) + " connected to: " + str(body))
            self.obj.set_pos(0,0,0)
            self.obj.set_rpy(math.pi/2,0,math.pi/2)

    def reset(self):
        #for debuggin moves model back the center of view (ctrl+r will accomplish the same thing)
        self.obj.set_pos(0,0,0)
        self.obj.set_rpy(math.pi/2,0,0)
        rospy.sleep(0.5) #waits for reset move to complete otherwise things get goofy

    def ABSmove(self, pos):
        #if a list is supplied then move uses absolute coordinates and moves the rover there.
        if len(pos) == 2:
            self.obj.set_pos(pos[0],pos[1])
        elif len(pos) == 3:
            self.obj.set_pos(pos[0],pos[1],pos[2])
        else:
            rospy.logerr(ValueError("List either has too few or too many values! Please supply either 2 or 3 cartesian coordinates."))
            raise ValueError("List either has too few or too many values! Please supply either 2 or 3 cartesian coordinates.")
        rospy.sleep(0.5)
        rospy.loginfo(self.obj.get_pos())

    def move(self,pos):
        rot = self.obj.get_rpy()
        currentPos = self.obj.get_pos()
        currentPos = Vector(round(currentPos.x,3),round(currentPos.y,3),round(currentPos.z,3)) #converts points msg to a vector while allows for simpler manipulation

        DVector = Vector( #Vector Constructer. Calculates X,Y components based off Yaw & Desired Move distance
        round(pos * (math.cos(rot[2])),3)
        ,round(pos * (math.sin(rot[2])),3)
        ,0
        )
        #self.obj.set_pos(DVector.x(),DVector.y(),0) #replace 0 with MovePos.z() for z component
        rospy.loginfo("Moving: \n dX: " + str(DVector.x()) + "\n dY: " + str(DVector.y()) + "\n RPY: " + str(rot))
        
        #error occurs when adding onto
        currentPos += DVector
        self.obj.set_pos(currentPos.x(),currentPos.y(),-1.03)
        rospy.loginfo(self.obj.get_pos())

    def debugMove(self):
        pass
        self.obj.set_rpy(math.pi/2,0,math.pi*3/4)
        self.obj.set_pos(self.obj.get_pos().x,self.obj.get_pos().y,0)
        rospy.loginfo(self.obj.get_pos())

    def rotate(self,rot):
        CurRot = self.obj.get_rpy()
        Drot = CurRot[2] + rot
        self.obj.set_rpy(CurRot[0],CurRot[1],Drot)




###MAIN###

def main():
    #inits AMBF client and connects to it. Declared globally so other functions can access it.
    global _client
    _client = Client()
    _client.connect()

    
    rospy.Subscriber("joy",Joy,JoyInput)

    Body = Movement("RoverBody")

    Body.ABSmove([0,0,0])
    while not rospy.is_shutdown():

        if Xb1.axes[1] != 0:
            Body.move(Xb1.axes[1])
            rospy.loginfo("Trying to move")
        if Xb1.buttons[0] == 1:
            Body.reset() #resets to (0,0,0) and RPY (0,0,0) activated with A button
            rospy.logwarn("Resetting Position to (0,0)")
        if Xb1.buttons[1] == 1:
            Body.ABSmove([float(input("X coord: ")),float(input("Y coord: ")),0]) #for debugging allows movement to custom coordinate activated with B button
        if Xb1.axes[3] != 0:
            Body.rotate(Xb1.axes[3]) #no need to normalize since it already is +- 1

        _client.clean_up()
        rate.sleep()
        
    #rospy.spin()

if __name__ == '__main__':
    rospy.init_node('rover')
    rospy.loginfo("Rover Node Started")
    #rospy.spin()
    try:
        rate = rospy.Rate(rospy.get_param("/rate")) #60 Hz refresh rate, similar to most common displays
    except:
        rospy.logwarn("\"/rate\" parameter not set, defaulting to 60hz")
    main()
