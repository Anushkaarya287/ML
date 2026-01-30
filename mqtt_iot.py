import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Sensor Data:", msg.payload.decode())


client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("iot/sensor1")

print("Connected to MQTT broker. Waiting for data...")

# start listening
client.loop_forever()
