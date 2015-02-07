#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button = False 
led = False

try:
   while True:
      button = GPIO.input(11)
      if button and led:
         GPIO.output(12, 0)
         led = False
         time.sleep(0.5)
      elif button:
         GPIO.output(12, 1)
         led = True
         time.sleep(0.5)
      else:
         time.sleep(0.5)
except KeyboardInterrupt:
   GPIO.cleanup()

