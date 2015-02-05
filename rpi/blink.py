#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

try:
   while True:
      GPIO.output(12, False)
      sleep(1)
      GPIO.output(12, True)
      sleep(1)

finally:
   GPIO.cleanup()