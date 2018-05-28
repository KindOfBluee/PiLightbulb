#!/usr/bin/python
import RPi.GPIO as GPIO

pinList = [2,3]

GPIO.setmode(GPIO.BCM)

for i in pinList:
    print(string(i)+" - ", end="")
    if(GPIO.input(i) == 0):
        print("LOW ", end="")
    else:
        print("HIGH ", end="")
    print(": " + string(GPIO.input(i)))
