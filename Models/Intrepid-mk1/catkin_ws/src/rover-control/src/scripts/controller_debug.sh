#sources ROS and the rest of BASH to make sure everythings there
#source ~/.bashrc

dir = /dev/input
joystick=$(ls /dev/input/js*)

echo $joystick
sudo jstest $joystick