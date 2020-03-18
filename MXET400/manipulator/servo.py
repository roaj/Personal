
#Import library
import RPi.GPIO as GPIO
import time

#setting up servo 
#using easy board settup
GPIO.setmode(GPIO.BOARD)

#pin 11 as output
GPIO.setup(11,GPIO.OUT)

#pin 11 and 50 the pwm frequency
servo_1 = GPIO.PWM(11,50) #PIN 11 , 50 HZ

#initialize servo bubt dont do anything 
servo_1.start(0)


def gripper_servo(servo_angle):

    angle = float(servo_angle)
    servo_1.ChangeDutyCycle(2+(angle/18))
    time.sleep(0.5)
    servo_1.ChangeDutyCycle(0)


try:
    while(True):
        gripper_servo(input("Enter Angle"))

finally:
    servo_1.stop()    
    GPIO.cleanup()
    print("goodbye!")


