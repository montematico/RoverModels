#!/usr/bin/python2.7

from ambf_client import Client
import rospy
from sensor_msgs.msg import Joy
from PyKDL import Vector, Wrench, Rotation
import math
import time

#takes message from control.py
#returns joint positions & confirmation


#just drag the tip and let the rest of the model follow along.
#add checks to make sure the tip doesnt get out of bounds.