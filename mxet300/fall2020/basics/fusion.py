#Sensor Fusion 
#purpose : show students how everything goes together on te scuttle
#Jorge Roa

# Import Internal Programs
import L2_kinematics as kin
import L2_log as log
import Lab3_gamepadControl as gp
# import L2_heading as heading
import numpy as np
import L1_adc as adc
# Import External programs
import numpy as np
import time


# DEFINE THE FUNCTIONS FOR THE PROGRAM
def mainTask():
  gp.manual_nav()
  pd = kin.getPdCurrent()
  frame = kin.getMotion()
  # headingAngle = headingVal()
  voltageJack = adc.getDcJack()
  ##/tmp/
  log.tmpFile(pd[0],"pdl.txt")
  log.tmpFile(pd[1],"pdr.txt")
  log.tmpFile(frame[0],"xdot.txt")
  log.tmpFile(frame[1],"tdot.txt")
  # log.tmpFile(headingAngle,"heading.txt")
  log.tmpFile(voltageJack,"vjack.txt")
  # headindLetter()
  
  
def headingVal():
  axes = heading.getXY()
  axesScaled = heading.scale(axes)
  h = heading.getHeading(axesScaled)
  headingDegrees = round(h*180/np.pi,2)
  return headingDegrees

def headindLetter():
  #get heading val determine what to do with it casestructure
  heading = headingVal()
  if (heading < 30) & (heading > -30):
    log.stringTmpFile("N","headingWord.txt")
  elif (heading < -30 )&(heading > -60):
    # headingWord = "NE"
    log.stringTmpFile("NE","headingWord.txt")
  elif (heading < -60) & (heading > -120):
    # headingWord = "E"
    log.stringTmpFile("E","headingWord.txt")
  elif (heading < -120) & (heading > -150):
    # headingWord = "SE"
    log.stringTmpFile("SE","headingWord.txt")
  elif (heading < -150) | (heading > 150):
    # headingWord = "S"
    log.stringTmpFile("S","headingWord.txt")
  elif (heading > 120) & (heading < 150):
    # headingWord = "SW"
    log.stringTmpFile("SW","headingWord.txt")
  elif (heading > 60) & (heading < 120):
    # headingWord = "W"
    log.stringTmpFile("W","headingWord.txt")
  elif (heading > 30) & (heading < 60):
    log.stringTmpFile("NW","headingWord.txt")
  
if __name__ == "__main__":
  while 1:
    # headingVal()
    mainTask()
    time.sleep(0.005) # delay a short period
