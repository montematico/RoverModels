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
    armBase_obj.set_pos(0,0,2)
    armBase_obj.set_rpy(toRad(90), 0, 0)

    
    print(armBase_obj.get_num_joints())
    print(armBase_obj.get_children_names())
    jointnum = input("what joint?")
    #jointnum = 4 #I'm not sure which joint I need to select so this is an interim solution
    armBase_obj.set_joint_pos(jointnum,0)
    armBase_obj.set_joint_effort(jointnum,5)
    while True:
        armBase_obj.set_joint_pos(jointnum,0)        
        #armrot = armBase_obj.get_rot() #returns a tuple with the RPY values of the armBase
        for x in range(-360,360,45):
            armBase_obj.set_joint_pos(jointnum,toRad(x))
            time.sleep(5)
            print('Current rotation = ' + str(toRad(x)) + ' radians')
        print('loop returned to 0deg')

    print('Exiting loop, cleaning up')
    _client.clean_up()
    time.sleep(1)
    exit()

if __name__ == '__main__':
    main()