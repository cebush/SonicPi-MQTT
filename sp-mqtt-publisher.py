import paho.mqtt.client as paho
import time, os, sys

topic = sys.argv[1]
filename = sys.argv[2]

host = "iot.eclipse.org"
client = paho.Client()
client.connect(host, 1883)

timestamp1 =  -10
while True:
    timestamp2 = os.path.getmtime(filename)
    if timestamp1 != timestamp2:
        with open(filename, 'r') as myfile:
            filedata=myfile.read()
        timestamp1 = timestamp2
    client.publish(topic, filedata)
    time.sleep(10)
