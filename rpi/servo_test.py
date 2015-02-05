#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

servo = GPIO.PWM(12, 50)
servo.start(7.5)

try:
   while True:
      servo.ChangeDutyCycle(7.5)
      time.sleep(1)
      servo.ChangeDutyCycle(12.5)
      time.sleep(1)
      servo.ChangeDutyCycle(2.5)
      time.sleep(1)

except KeyboardInterrupt:
   servo.stop()
   GPIO.cleanup()
