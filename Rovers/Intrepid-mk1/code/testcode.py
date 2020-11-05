from ambf_client import Client
import keyboard #used for keyboard events to read keyboard input. FIND A LIBRARY THAT WORKS
import time

#Creates a client and connects to it
_client = Client()
_client.connect()


#.set_pos() origin is the center
#.set_rpy() uses radiians. Also RPY is roll pitch yaw.

print('Client connected\n')
print('Listing objects: \n' + str(_client.get_obj_names()))


def toRad(deg):
    #function to convert from degrees to radians since I didn't pay enough attention in triginometry last year
    return deg*(3.14159/180)
def main():
    #test code -- should rotate armaround in circles
    armBase_obj = _client.get_obj_handle('ambf/env/armBase')
    armBase_obj.set_pos(0,0,5)
    armBase_obj.set_rpy(toRad(90), 0, 0)
    print('starting loop')
    i = 0
    armroll = toRad(90)
    while True:
        armrot = armBase_obj.get_rot() #returns a tuple with the RPY values of the armBase
        armroll += toRad(10)
        armBase_obj.set_rpy(armroll, 0, 0) #should chage only the roll value of the arm
        time.sleep(0.5)
        i += 1
        print(i)
    print('Exiting loop, cleaning up')
    _client.clean_up()
    time.sleep(1)
    exit()

if __name__ == '__main__':
    main()