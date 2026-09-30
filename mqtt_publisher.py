import time
import paho.mqtt.client as mqtt
from sensor_simulator import generate_readings

client = mqtt.Client()
client.connect("localhost", 1883)

readings = generate_readings()

for r in readings:
    message = f"{r['equipment_id']},{r['temperature']},{r['vibration']}"
    client.publish("sensors/readings", message)
    print("Sent:", message)
    time.sleep(1)

client.disconnect()