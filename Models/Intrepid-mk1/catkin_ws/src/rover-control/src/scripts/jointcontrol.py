#!/usr/bin/python2.7

#A script to allow for controlling of the rover using joystick inputs.
#will eventually be broken into several seperate scripts with topics and services to
# allow for easily switching control inputs or rover in and out 

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy



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
try:
    _client = Client()
    _client.connect()
except:
    rospy.logwarn("ERROR CONNECTING TO AMBF CLIENT!")
else:
    rospy.loginfo("Created and Connected to AMBF client.")
    rospy.loginfo(_client.get_obj_names())
    RoverBody =_client.get_obj_handle('RoverBody')


#Joint Class to (hopefully) make adressing several joints easier.
class Joint:
    obj = None
    jointidx = 0
    def __init__(self, body,joint):
        #creates an obj for ambf to work with. 
        #Also has ****very basic***** error checking since idk how to do anything more advanced
        try:
            Joint.obj = _client.get_obj_handle(body)
            Joint.jointidx = joint
        except:
            rospy.logwarn("An Error Occured while creating joint!")
        else:
            rospy.loginfo("New Joint created \n body: " + str(body) + "\n idx: " + str(joint))

    def get_joint_pos():


    def move(self, pos,torque = 0):
        #sets position for joint to travel to, also optionally pass torque parameter
        self.obj.set_joint_pos(self.jointidx, self.obj.get_joint_pos() + pos) #get_joint_pos doesn't work. Use rostopics /ambf/env/*Parentname*/state
        if torque != 0:
            self.obj.set_joint_effort(self.jointidx, torque)
    
    def setTorque(self, force):
        #sets the torque acting on a joint.
        self.obj.set_joint_effort(self.jointidx, force)

class Wheels(Joint):
    pass
    #create a wheel class to adress several wheels





###MAIN###

def main():
    
    _client = Client()
    _client.connect()
    wheel = Joint("/ambf/env/2WheelSpringRight",0)
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
