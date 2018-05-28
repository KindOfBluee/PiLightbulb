#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [3]

# loop through pins and set mode

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

def trigger() :
        for i in pinList:
          GPIO.output(i, GPIO.HIGH) #?
#          GPIO.cleanup()

try:
    trigger()

except KeyboardInterrupt:
  print("Quit")
  # Reset GPIO settings
  GPIO.cleanup()
