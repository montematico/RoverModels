#!/usr/bin/python2.7

#A script to allow for controlling of the rover using joystick inputs.
#will eventually be broken into several seperate scripts with topics and services to
# allow for easily switching control inputs or rover in and out 

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation


axes = 0.0 #sets axes to a float
buttons = None
##################################################################
###################### JOYSTICK INPUT ############################
##################################################################
input = Joy()
def JoyInput(data):
    rospy.loginfo(data.axes)
    rospy.loginfo(data.buttons)
    axes = data.axes[1]
    buttons = data.buttons[2]

#subscribes to joy topic
joysub = rospy.Subscriber("joy",Joy,JoyInput)

##################################################################
####################### Rover Control ############################
##################################################################
#Create a class with an innit with subscribes to a specific joint
class JointPos:
    #this is gonna be a pain in the ass to make
    #__init__ should create a new subscriber with a callback on self.jointCallback
    #maybe make this a child of Joint to make things prettier.
    #ask Mentor about cleaner way of subscribing to several topics
    def __init__(self,Topic):
        jointsub = rospy.Subscriber(str(Topic),Topic,self.jointCallback)
    def jointCallback(self,data):
        data
        pass

#creates an AMBF client and tries to connects to it

class Movement:
    obj = None
    jointidx = 0
    def __init__(self, body):
        #creates an obj for ambf to work with. 
        #Also has ****very basic***** error checking since idk how to do anything more advanced
        try:
            self.obj = _client.get_obj_handle(body)
        except:
            rospy.logwarn("An Error Occured while creating joint!")
        else:
            rospy.loginfo("Body: " + str(self) + " connected to: " + str(body))

    def move(self, pos):
        if type(pos) == 'list':
            #if a list is supplied then move uses absolute coordinates and moves the rover there.
            if len(pos) == 2:
                self.obj.set_position(pos[0],pos[1])
            elif len(pos) == 3:
                self.obj.set_position(pos[0],pos[1],pos[2])
            else:
                rospy.logerr(ValueError("List either has too few or too many values! Please supply either 2 or 3 cartesian coordinates."))
                raise ValueError("List either has too few or too many values! Please supply either 2 or 3 cartesian coordinates.")
        else:
            pass
            #if a single coordinate is provided then the rover simply moves forward that distance
            #eventually I'll make this support 3d coordinates but right now it only supports 2d movement.
            #moveVector = Vector(0,0,0)
            #rot = self.obj.get_rpy()
            
            #rot.pop(0) #removes the roll component since it's unnececary
            #pitch = y, yaw = x





###MAIN###

def main():
    
    _client = Client()
    _client.connect()
    wheel = Joint("/ambf/env/Body")
    #wheel.setTorque()
    print("got here")
    while not rospy.is_shutdown():
        print "into loop"
        rospy.loginfo(axes)
        if abs(axes) >= 1000:
            wheel.move(500)
        else:
            wheel.move(-500)

        _client.clean_up()
        rate.sleep()

if __name__ == '__main__':
    #rospy.init_node('rover')
    rospy.loginfo("Rover Node Started")
    #rospy.spin()
    rate = rospy.Rate(60) #60 Hz refresh rate, similar to most common displays
    main()
