import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"Publisher Eliana")

# client.connect(endereço broker, porta, keep alive)
client.connect("localhost", 1883)

client.publish("testing", "Hello Python")

client.loop_start()