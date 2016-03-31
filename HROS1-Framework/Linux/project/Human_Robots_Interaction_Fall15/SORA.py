import pexpect 
import ctypes 
import api 
import os 
import time
import sys 
import struct 
import time

def Main():
        try:
                if api.Initialize():
                        print("Initialized")
                else:
                        print("Initialzation Failed")
		get_sentence()
        except KeyboardInterrupt:
                api.ServoShutdown()
                sys.exit()
        except():
                api.ServoShutdown()
                sys.exit()

def get_sentence():
        while True:
                try:
			child = pexpect.spawn ('sudo python /home/pi/HROS1-Framework/Linux/project/pixy/build/libpixyusb_swig/get_blocks.py')
			i = child.expect(['SIG=7'])
                        if i == 0:
				api.PlayAction(15)
				child.close(force=True)
	                        break
                except KeyboardInterrupt:
                        child.close(force=True)
                        break



if __name__ == "__main__":
	Main()
