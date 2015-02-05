#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
   while True:
      if GPIO.input(11):
         print "Pin 11 is: HIGH - LED ON"
         GPIO.output(12, 1)
      else:
         print "Pin 11 is: LOW - LED OFF"
         GPIO.output(12, 0)
      sleep(0.1)
finally:
   GPIO.cleanup()
