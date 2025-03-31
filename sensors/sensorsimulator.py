import random
import paho.mqtt.publish as publish
import time

while True:
    # Generate realistic sensor values
    co2 = random.randint(400, 2000)      # Normal: 400-1000ppm
    pm = random.randint(10, 100)         # Normal: <35µg/m³
    voc = random.uniform(0.1, 2.0)       # Normal: <0.5ppm
    
    # Publish to MQTT
    publish.single("home/airquality/co2", co2, hostname="localhost")
    publish.single("home/airquality/pm", pm, hostname="localhost")
    publish.single("home/airquality/voc", voc, hostname="localhost")
    
    print(f"Published: CO2={co2}, PM={pm}, VOC={voc:.2f}")
    time.sleep(5)  # Send data every 5 seconds