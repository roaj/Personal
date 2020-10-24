#inport external libs
import RPi.GPIO as GPIO
import time
import L1_gamepad as gp
# import time

#local libs


#initializaiton 
element = False
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz 
#start duty cycle
p.start(7.5) # 0 



def getJoy():
    GpData = gp.getGP()
    b = GpData[4]
    # print(b)
    if b == 1:
        element = True
    else:
        element = False
    return

def moveServo():
    #0.5(2.5%) / 1.5(7.5) / 2.5(12.5)
    GpData = gp.getGP()
    b = GpData[4]
    if b == 1:
        # print("here")
        p.ChangeDutyCycle(12.5)
        # time.sleep(0.5)

    return

if __name__ == "__main__":
    while True:
        try:
            # getJoy()
            moveServo()
            time.sleep(0.1)
            # time.sleep(0.1)
        except KeyboardInterrupt:
            # p.stop()
            # GPIO.cleanup()
            pass
        finally:
            GPIO.cleanup()
