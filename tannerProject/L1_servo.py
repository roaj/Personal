import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(12.5) # Initialization
p.stop()
GPIO.cleanup()

if __name__ == "__main__":
  while True:
    try:
      p.ChangeDutyCycle(5)
      time.sleep(0.5)
      p.ChangeDutyCycle(7.5)
      time.sleep(0.5)
      p.ChangeDutyCycle(10)
      time.sleep(0.5)
    except KeyboardInterrupt:
      p.stop()
      GPIO.cleanup()
  pass
