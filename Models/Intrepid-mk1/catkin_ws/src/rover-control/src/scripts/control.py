#A script to allow for controlling of the rover using joystick inputs.
#will eventually be broken into several seperate scripts with topics and services to
# allow for easily switching control inputs or rover in and out 

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy






##################################################################
###################### JOYSTICK INPUT ############################
##################################################################
input = Joy()
def JoyInput(data):
    input.axes() = data.axes()
    input.buttons() = data.buttons()

#subscribes to joy topic
sub = rospy.Subscriber("joy",Joy,JoyInput)
rospy.spin()

##################################################################
####################### Rover Control ############################
##################################################################

rate = rospy.Rate(60) #60 Hz refresh rate, similar to most common displays

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
    obj
    jointidx = void
    def __init__(body,joint):
        #creates an obj for ambf to work with. 
        #Also has ****very basic***** error checking since idk how to do anything more advanced
        try:
            obj = _client.get_obj_handle(body)
            jointidx = joint
        except:
            rospy.logwarn("An Error Occured while creating joint!")
        else:
            rospy.loginfo("New Joint created \n body: " + body, "\n idx: " + joint)


    def move(pos,torque = 0):
        #sets position for joint to travel to, also optionally pass torque parameter
        obj.set_joint_pos(jointidx, obj.get_joint_pos() + pos)
        if torque != 0:
            obj.set_joint_effort(jointidx, torque)
    
    def settorque(torque):
        #sets the torque acting on a joint.
        obj.set_joint_effort(jointidx, torque)

def main():
    while not rospy.is_shutdown():
        
        #foo bar
        #current joint position + (joy_pos * scaler)
        _client.clean_up()


if __name__ == '__main__':
	rospy.init_node('rover')
	rospy.loginfo("Rover Node Started")
    main()