import paho.mqtt.client as paho
import sys, subprocess

def on_message(client, userdata, message):
    pipe = subprocess.Popen("sonic_pi", stdin=subprocess.PIPE, shell=True)
    pipe.communicate(input=message.payload)
    print(str(message.payload.decode("UTF-8")))

def on_disconnect(client, userdata, rc):
    subprocess.call("sonic_pi stop", shell=True)

topic = sys.argv[1]
host = "iot.eclipse.org"
client = paho.Client()
client.connect(host, 1883)
client.subscribe(topic, 0)

client.on_message = on_message
client.on_disconnect = on_disconnect

print("Press Ctrl-C to stop...")
try:
    client.loop_forever()
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
