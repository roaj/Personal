import time
import serial
import paho.mqtt.client as paho

# Setup MQTT
broker="broker.hivemq.com"
port=1883

topic = "scuttle/infrastructure/data/001/scale/latest"

def on_publish(client,userdata,result):         # create function for callback
    pass

mqtt = paho.Client()                          # create client object
mqtt.on_publish = on_publish                  # assign function to callback
mqtt.connect(broker,port)                     # establish connection

ser = serial.Serial('/dev/ttyUSB0',38400)

if __name__ == "__main__":
    while 1:
        weight = ser.readline().decode('utf-8')
        print("Weight Station Reading: " + weight)
        # time.sleep(0.01)
        mqtt.publish(topic, str(weight))

ser.close()
