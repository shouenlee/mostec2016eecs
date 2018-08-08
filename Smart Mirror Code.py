import sys
import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.OUT)

timeOffDelay = 120 #seconds
sensor = 25 #GPIO pin for sensor
led = 4 #GPIO pin for led

timeLastDetection = time.time()
screenState = 1

def screenOn():
    subprocess.call("xset dpms force on" , shell = True, stderr=subprocess.PIPE)

def screenOff():
    subprocess.call("xset dpms force off" , shell = True, stderr=subprocess.PIPE)
    

try:
    while True:
        if GPIO.input(sensor) == 1:
            timeLastDetection = time.time()
            GPIO.output(led,1)
            #time.sleep(1)
            #GPIO.output(led,0)
            if screenState == 0:
                screenOn()
                screenState = 1
        if time.time() - timeLastDetection > 5: #timeOffDelay:
            screenOff()
            screenState = 0
            GPIO.output(led,0)
except KeyboardInterrupt:
    GPIO.cleanup()
