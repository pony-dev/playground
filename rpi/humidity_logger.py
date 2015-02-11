#!/usr/bin/python

import sys
import time
import datetime
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

try:
   while True:
      f = open("humidity.log", "w")
      if humidity is not None and temperature is not None:
         f.write('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity) + "\n")
         time.sleep(10)
      else:
         print 'error'

except KeyboardInterrupt:
   f.close()
