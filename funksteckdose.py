#!/usr/bin/python
# -*- coding: utf-8 -*-
### funksteckdose.py ###

import RPi.GPIO as GPIO
import os
import time

# GPIO init
GPIO.setmode(GPIO.BOARD)

names = ["Kühltruhe kalt", "Kühlschrank kalt","Kühlschrank warm", "Kühltruhe warm"]
inputPins = [37,35,31,40]
codes = ["11110 1","11110 2","11110 3","11110 4"]
states = [0,0,0,0]

for i, inputPin in enumerate(inputPins):
  GPIO.setup(inputPin, GPIO.IN)

# endlessly repeat the signals every five seconds
while True:
    for i, inputPin in enumerate(inputPins):
        state = GPIO.input(inputPin)
        os.system("sudo /home/pi/raspberry-remote/send "+ codes[i] + " " + str(state))
        time.sleep(5)
