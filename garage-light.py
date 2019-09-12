import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
green = 17
yellow = 27
red = 22


GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

def green_light():
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(yellow, GPIO.LOW)

def yellow_light():
    GPIO.output(green, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(yellow, GPIO.HIGH)

def red_light():
    GPIO.output(green, GPIO.LOW)
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(yellow, GPIO.LOW)


def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time () 

    sig_time = end - start
    #cm 
    distance = sig_time / 0.000058 
    print('Distance: {} cm'.format(distance))
    return distance

while True:
    distance = get_distance()
    time.sleep (0.05)

    if distance >= 9 :
        green_light()
    elif 9 > distance > 6:
        yellow_light()
    elif distance <= 6:
        red_light()

while True:
    distance = get_distance()
    time.sleep (0.05)

    if distance >= 9 :
        green_light()
    elif 9 > distance > 6:
        yellow_light()
    elif distance <= 6:
        red_light()



