import paho.mqtt.client as mqtt
from database import get_connection, save_reading

conn = get_connection()
cursor = conn.cursor()

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    equipment_id, temperature, vibration = payload.split(",")
    print("Received:", payload)
    save_reading(cursor, equipment_id, float(temperature), float(vibration), "OK")
    conn.commit()

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensors/readings")
client.on_message = on_message

client.loop_forever()