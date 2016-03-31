import pexpect 
import ctypes 
import api 
import os 
import time
import sys 
import struct 

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
	child = pexpect.spawn ('julius -input mic -C /home/pi/voxforge/SORA/Sample.jconf')
        while True:
                try:
			i = child.expect(['sentence1: <s> SORA SIT </s>', 'sentence1: <s> SORA STAND </s>', 'sentence1: <s> SORA MOVE </s>', 'sentence1: <s> SORA STOP </s>'])
                        if i == 0:
                                api.PlayAction(15)
                                print "Sit"
                        elif i == 1:
                                api.PlayAction(8)
                                print "Stand up"
                        elif i == 2:
                                api.Walk(1)
				api.WalkMove(1)
                                print "Start Walking"
                        elif i == 3:
                                api.Walk(-1)
                                print "Stop Walking"
                except KeyboardInterrupt:
                        child.close(force=True)
                        break



if __name__ == "__main__":
	Main()
