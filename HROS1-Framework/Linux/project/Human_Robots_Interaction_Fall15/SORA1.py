import pexpect 
import ctypes 
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
	speed = 0
        while True:
                try:
			child = pexpect.spawn ('julius -input mic -C /home/pi/voxforge/test/Sample.jconf')
			i = child.expect(['sentence1: <s> RED', 'sentence1: <s> BLUE', 'sentence1: <s> PUSH'])
                        if i == 0:
                                print "red ==========>"
                        elif i == 1:
                                print "blue ====>"
                        elif i == 2:
                                print "push ======>"
                except KeyboardInterrupt:
                        child.close(force=True)
			api.ServoShutdown()
	                sys.exit()
                        break



if __name__ == "__main__":
	get_sentence()
