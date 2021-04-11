# Lab4Template.py
# Team Number:
# Hardware TM:
# Software TM:
# Date:
# Code purpose: 

# Import Internal Programs
import L2_kinematics as kin
import L2_log as log

# Import External programs
import numpy as np
import time

# DEFINE THE FUNCTIONS FOR THE PROGRAM
def task2():
  pd = kin.getPdCurrent()
  motion = kin.getMotion()
  print ("pdr: ",pd[0],"pdl: ",pd[1],"xdot: ", motion[0], "thetaDot: ", motion[1])
  #do some items here

# UNCOMMENT THE LOOP BELOW TO RUN THE PROGRAM CONTINUOUSLY
while 1:
    task2()
    time.sleep(0.2) # delay a short period
