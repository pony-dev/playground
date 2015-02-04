from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while 1:
  GPIO.output(12, False)
  sleep(1)
  GPIO.output(12, True)
  sleep(1)
