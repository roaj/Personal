import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

import socket

UDP_IP = "192.168.8.55"
UDP_PORT = 5005

f = open("RTIMULib.ini", "r")
settings = f.readline()
f.close()


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

SETTINGS_FILE = "RTIMULib"

while 1:
  print("Using settings file " + SETTINGS_FILE + ".ini")
  if not os.path.exists(SETTINGS_FILE + ".ini"):
    print("Settings file does not exist, will be created")

  s = RTIMU.Settings(SETTINGS_FILE)
  imu = RTIMU.RTIMU(s)

  print("IMU Name: " + imu.IMUName())

  if (not imu.IMUInit()):
      print("IMU Init Failed");
      sys.exit(1)
  else:
      print("IMU Init Succeeded");

  poll_interval = imu.IMUGetPollInterval()
  print("Recommended Poll Interval: %dmS\n" % poll_interval)

  while True:
    if imu.IMURead():
      # x, y, z = imu.getFusionData()
      # print("%f %f %f" % (x,y,z))
      data = imu.getIMUData()

      # print(data)

      fusionPose = data["fusionPose"]
#      print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]),
#          math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))

      MESSAGE = (str(round(math.degrees(fusionPose[0]),1))+','+str(round(math.degrees(fusionPose[1]),1))+','+str(round(-1*math.degrees(fusionPose[2]),1)))

      # print(MESSAGE)

      sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))

      f = open("RTIMULib.ini", "r")
      settings2 = f.readline()
      f.close()

      if settings2 != settings:
        break
      if not (fusionPose[0] and fusionPose[1] and fusionPose[2]):
        break

      # fusionPose = data["accel"]
      # print("r: %f p: %f y: %f" % (fusionPose[0], fusionPose[1], fusionPose[2]))

      #time.sleep(poll_interval*1.0/1000.0)
      time.sleep(0.05)

  time.sleep(0.1)





