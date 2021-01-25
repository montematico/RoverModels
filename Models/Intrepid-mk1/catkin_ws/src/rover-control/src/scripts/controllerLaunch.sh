#!/bin/bash

#starts the joy node so ROS can take controller input

#gets joy port
dir = /dev/input
joystick=$(ls /dev/input/js*)

#sets the parameters and starts the joy node

rosparam set joy_node/dev $joystick
echo "Joy node started at: " $joystick
rosrun joy joy_node