#!/usr/bin/python3
import pyaudio
import audioop
import wave
import api
import sys

CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 5
#WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD = 4000

flag = 0

try:
  if api.Initialize():
    print("Initalized")
  else:
    print("Intialization failed")
except (KeyboardInterrupt):
  api.ServoShutdown()
  sys.exit()


p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	dev = p.get_device_info_by_index(i)
	print((i, dev['name'],dev['maxInputChannels']))

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
		input_device_index = 0,
                frames_per_buffer=CHUNK)

print("* recording")

while True:
    try:
    	data = stream.read(CHUNK)
    except IOError as ex:
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 0,
                frames_per_buffer=CHUNK)	
#    except(KeyboardInterrupt):
#        stream.stop_stream()
#        stream.close()
#        p.terminate()
	data = stream.read(CHUNK)
		
    rms = audioop.rms(data, 2)
    print(rms)
    if(rms>THRESHOLD and flag == 0):
      print 'Standing'
      api.PlayAction(8)
      print 'Walking'
      api.Walk(1)
      api.WalkTurn(-18)
      api.WalkMove(20)
      flag = 1
    elif(rms>THRESHOLD and flag == 1):
      print 'Stopping'
      api.Walk(0)
      print 'Sitting'
      api.PlayAction(15)
      flag = 0
    	


