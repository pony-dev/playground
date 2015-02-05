#!/usr/bin/python

# Importing librarys
from time import sleep
import RPi.GPIO as GPIO

# Setting up GPIO pins
GPIO.setmode(GPIO.BOARD)	# 
GPIO.setup(12, GPIO.OUT)	# set pin 12 as output

try:
   while True:			# loops until interrupt (Ctrl+C)
      GPIO.output(12, False)	# set pin 12 low
      sleep(1)			# wait 1s
      GPIO.output(12, True)	# set pin 12 high
      sleep(1)			# wait 1s

finally:
   GPIO.cleanup()
