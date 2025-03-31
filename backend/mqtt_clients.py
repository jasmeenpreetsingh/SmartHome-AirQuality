import paho.mqtt.client as mqtt
from django.conf import settings
from .models import SensorData

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("home/airquality/#")

def on_message(client, userdata, msg):
    topic = msg.topic
    value = float(msg.payload.decode())
    
    # Create new SensorData entry
    data = SensorData()
    
    if "co2" in topic:
        data.co2 = value
        if value > 1000:
            data.action_taken = "HVAC activated"
    elif "pm" in topic:
        data.particulate_matter = value
        if value > 35:
            data.action_taken = "Air purifier activated"
    elif "voc" in topic:
        data.voc = value
        if value > 0.5:
            data.action_taken = "Windows opened"
    
    data.save()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect using settings from settings.py
client.connect(
    settings.MQTT_BROKER,
    settings.MQTT_PORT,
    60
)
client.loop_start()