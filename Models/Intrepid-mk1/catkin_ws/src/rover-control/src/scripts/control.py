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
    axes = [0,0] 
    buttons =[0,0] 

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
        #for debuggin moves model back the center of view
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
    def move(self,pos):
        #if a single coordinate is provided then the rover simply moves forward that distance
        #eventually I'll make this support 3d coordinates but right now it only supports 2d movement.
    
        #takes the Yaw and desired move distance then calculates the X and Y component of the move.
        rot = self.obj.get_rpy()
        Dxyz = [
        round(pos * math.sin(rot[2] - (math.pi/2)),3)
        ,round(pos * math.cos(rot[2] - (math.pi/2)),3)
        #,pos * math.sin(rot[1]) The Z component unnececary
        ]
        ignoreMove = False
        
        #since this adds to the current position even if no change is needed it will move.
        #this check skips the move unless there is a significant change in the move
        for i in Dxyz:
            if abs(i) <= 0.1:
                ignoreMove = True
            else:
                ignoreMove = False
                break
        if not ignoreMove:
            currentPOS = self.obj.get_pos() #not a list, geometry_msgs/Point.msg
            moveCoord = [Dxyz[0] + currentPOS.x ,Dxyz[1] + currentPOS.y ,0]
            rospy.loginfo(moveCoord)
            rospy.loginfo("Moving: \n dX: " + str(Dxyz[0]) + "\n dY: " + str(Dxyz[1]) + "\n RPY: " + str(rot))
            self.obj.set_pos(moveCoord[0],moveCoord[1],0)
        
    def move2(self,pos):
        rot = self.obj.get_rpy()
        currentPos = self.obj.get_pos()
        currentPos = Vector(currentPos.x,currentPos.y,currentPos.z)

        DVector = Vector( #vector constructer
        round(pos * (math.cos(rot[2])),3)
        ,round(pos * (math.sin(rot[2])),3)
        ,0
        )
        MovePos = currentPos + DVector
        self.obj.set_pos(MovePos.x(),MovePos.y(),0) #replace 0 with MovePos.z() for z component
        rospy.loginfo("Moving: \n dX: " + str(DVector.x()) + "\n dY: " + str(DVector.y()) + "\n RPY: " + str(rot))
        rospy.loginfo(MovePos)


    def debugMove(self):
        self.obj.set_rpy(math.pi/2,0,0)
        #self.obj.set_pos(self.obj.get_pos().x,self.obj.get_pos().y,0)





###MAIN###

def main():
    #inits AMBF client and connects to it. Declared globally so other functions can access it.
    global _client
    _client = Client()
    _client.connect()

    
    rospy.Subscriber("joy",Joy,JoyInput)

    wheel = Movement("RoverBody")

    wheel.ABSmove([0,0,0])
    while not rospy.is_shutdown():
        wheel.debugMove()
        #rospy.logwarn(Xb1.axes)
        #rospy.logwarn(Xb1.buttons)

        if Xb1.axes[1] != 0:
            wheel.move2(Xb1.axes[1])
            rospy.loginfo("Trying to move")
        if Xb1.buttons[0] == 1:
            wheel.reset() #resets to (0,0,0) and RPY (0,0,0) activated with A button
            rospy.logwarn("Resetting Position to (0,0)")
        if Xb1.buttons[1] == 1:
            wheel.ABSmove([float(input("X coord: ")),float(input("Y coord: ")),0]) #for debugging allows movement to custom coordinate activated with B button

        _client.clean_up()
        rate.sleep()
        
    #rospy.spin()

if __name__ == '__main__':
    rospy.init_node('rover')
    rospy.loginfo("Rover Node Started")
    #rospy.spin()
    rate = rospy.Rate(60) #60 Hz refresh rate, similar to most common displays
    main()
