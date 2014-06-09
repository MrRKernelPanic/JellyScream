import time
import RPi.GPIO as GPIO
import os
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
#   Set pin 3 on the GPIO header to be an input
GPIO.setup(3,GPIO.IN)
#   Connect other wire to Pin25 on GPIO!
while True:
       if GPIO.input(3) == False:
                #os.system(.mpg321 la.mp3 &.)
                print .Ouch! Stop it!.
       time.sleep(0.1)
