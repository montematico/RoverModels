from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy



def WheelControl(pos, effort, side = "both"):
    #There is definitly a better way to do this but I can't think of it
    bodies = _client.get_obj_names()
    WS = [_client.get_obj_handle(bodies[4]),_client.get_obj_handle(bodies[8]),_client.get_obj_handle(bodies[17],_client.get_obj_handle(bodies[6]]
           #1WheelSpringLeft                    #2WheelSpringLeft                  #1WheelSpringRight               #2WheelSpringRight
    

if __name__ == '__main__':
	rospy.init_node('rover')
	rospy.loginfo("Rover Node Started")


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

    class Tire:
        

    while not rospy.is_shutdown():
        #foo bar
        #current joint position + (joy_pos * scaler)

    _client.clean_up()

