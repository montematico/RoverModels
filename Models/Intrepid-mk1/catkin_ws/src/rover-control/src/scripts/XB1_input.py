#this may not be needed

import rospy
from sensor_msgs.msg import Joy
from sensor_msgs.msg import Int16MultiArray

if __name__ == '__main__':
    rospy.init_node('Controller_input')
    rospy.loginfo("XBox 1 Controller Input has been started")

    rate = rospy.Rate(60) #60 Hz refresh rate, similar to most common displays

    #creates publisher topic on "/controller_input"
    pub = rospy.Publisher('/controller_input', std_msgs.msg.Joy, queue_size= 10)

    #subscribes to joy topic
    sub = rospy.Subscriber("joy_str")
    while not rospy.is_shutdown():
        #should subscribe to Joy topic and forward it to the "brain". Done in such a roundabout way so that different controllers or even a keyboard can more easily be swapped in.

        #Should take the controls for Joy package and import it into
        #check data Type controller has 8 signed 16 bit values & 11 bool buttons.
 

        msg = Joy()
        msg.axes() = []
        msg.buttons

        pub.publish(msg)
        rate.sleep()