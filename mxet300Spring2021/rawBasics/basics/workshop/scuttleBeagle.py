#!/usr/bin/env python3
# import python libraries
import time, math
import getopt, sys

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.servo as servo
import rcpy.clock as clock

# class ScuttleServo:

#     def __init__(self):
#         rcpy.set_state(rcpy.RUNNING)
#         self.duty = 1.5
#         self.period = 0.02
#         self.channel = 0

#     def setServoChannel(self,channel=1):
#         self.channel = channel        
#         self.srvo = servo.Servo(self.channel)
#         return

#     ###duty = position( -1.5 - 1.5 ) | negative --> CCW | positive --> CW 
#     def move2(self,duty):
#         self.duty = duty

#         self.srvo.set(self.duty)
#         servo.enable()
#         self.clck = clock.Clock(self.srvo, self.period)
#         self.clck.start()
#         time.sleep(1)
#         # keep running
#         # while rcpy.get_state() != rcpy.EXITING:
#         #     print("jorge")
#         #     # sleep some
#         #     time.sleep(1)
#         # return

# s = ScuttleServo()
# s.setServoChannel()
# s.move2(-1.5)
duty = 1.5
period = 0.02
channel = 0
sweep = False
brk = False
free = False
rcpy.set_state(rcpy.RUNNING)
srvo = servo.Servo(channel)

# def setServoChannel(channel=1):
def setDuty(duty):
    srvo.set(duty)
    servo.enable()
    clck = clock.Clock(srvo, period)
    clck.start()   

# setServoChannel()
setDuty(1.5)
time.sleep(2)
setDuty(-1.5)
time.sleep(2)
setDuty(1.5)