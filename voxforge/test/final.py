import pexpect
import ctypes
from pixy import *
from ctypes import *
import api
import os
from time import sleep
import sys
import struct


class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]
# Pixy Python SWIG get blocks example #

def Main():

  print ("Start initialization")

# Initialize Pixy Interpreter thread #
  pixy_init()
  print ("Pixy initialized")

# Initialize Servos #
  try:
    if api.Initialize():
      print("api initalized")
      get_sentence()
    else:
      print("api intialization failed")
  except (KeyboardInterrupt):
    api.ServoShutdown()
    sys.exit()
  except():
    api.ServoShutdown()
    sys.exit()


def get_sentence():
  flag_c = 0
  while True:
    try:
      child = pexpect.spawn ('julius -input mic -C /home/pi/voxforge/Final/Sample.jconf')
      i = child.expect(['sentence1: <s> START'])
      if i == 0:
        api.PlayAction(8)
        print "Start checking the signs.."
	start_check()
    except KeyboardInterrupt:
      child.close(force=True)
      api.ServoShutdown()
      sys.exit()
      break

def start_check():
  blocks = BlockArray(100)
  frame  = 0
  green_flag = 0;
#  stand_flag = 0
#  walk_flag = 0
  # Wait for blocks #
  while 1:
    count = pixy_get_blocks(100, blocks)
    if count == 1:
      # Blocks found #
      #print 'frame %3d:' % (frame)
      frame = frame + 1
      for index in range (0, count):
        #print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height)
        if green_flag == 0:
          if blocks[index].signature == 4:
            print 'Green sign founded, start walking...'
            sleep(1)
            print 'Walking'
            api.Walk(1)
            print 'Moving'
            api.WalkMove(5)       
            green_flag = 1
        elif green_flag == 1:
          if blocks[index].signature == 1:
            print 'Red sign founded, stop walking'
            sleep(1)
            api.Walk(0)
            stand_flag = 0

if __name__ == "__main__":
  Main()

#        if stand_flag == 0:
#          if blocks[index].signature == 5:
#            print 'Standing'
#            api.PlayAction(8)
#            sleep(1)
#            print 'Walking'
#            api.Walk(1)
#            print 'Moving'
#            api.WalkTurn(-10)
#            api.WalkMove(15)       
#           stand_flag = 1
#        elif stand_flag == 1:
#          if blocks[index].signature == 1:
#            print 'Stopping'
#            api.Walk(0)
#            sleep(1)
#            print 'Sitting'
#            api.PlayAction(15)
#            stand_flag = 0
          


   #    elif stand_flag == 1:
   #     if blocks[index].signature == 6 and blocks[index].width < 100 and walk_flag == 0:
   #       print 'Start Walking'
   #       api.Walk(1)
   #       walk_flag = 1
   #     elif blocks[index].signature == 6 and blocks[index].width < 100 and walk_flag == 1:
   #       print 'Start Moving'
   #       print blocks[index].width         
   #       api.WalkMove(5)
   #     elif blocks[index].signature == 6 and blocks[index].width >= 100 and walk_flag == 1:
   #       print 'Stop Walking'
   #       api.Walk(0)
   #       walk_flag = 0
   #     elif blocks[index].signature == 1 and walk_flag == 0:
   #       print 'Sitting'
   #       api.PlayAction(15)
   #       stand_flag = 0
