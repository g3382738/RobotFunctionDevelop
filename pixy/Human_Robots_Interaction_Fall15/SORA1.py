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
			child = pexpect.spawn ('julius -input mic -C /home/pi/voxforge/SORA/Sample.jconf')
			i = child.expect(['sentence1: <s> SORA SIT', 'sentence1: <s> SORA STAND', 'sentence1: <s> SORA MOVE', 'sentence1: <s> SORA STOP'])
                        if i == 0:
                                api.PlayAction(15)
                                print "Sit"
                        elif i == 1:
                                api.PlayAction(8)
                                print "Stand up"
                        elif i == 2:
                                api.PlayAction(33)
                                print "Start Moving"
                        elif i == 3:
                                api.PlayAction(32)
                                print "why?"
                except KeyboardInterrupt:
                        child.close(force=True)
                        break



if __name__ == "__main__":
	Main()
