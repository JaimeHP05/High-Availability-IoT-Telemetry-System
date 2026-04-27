import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "localhost"
TOPIC = "telemetry/environmental"

client = mqtt.Client()

try:
    client.connect(BROKER, 1883, 60)
    print("Sensor simulator running. Press Ctrl+C to stop.")
    
    while True:
        payload = {
            "sensor_id": "station_01",
            "temp": round(random.uniform(20.0, 25.0), 2),
            "hum": round(random.uniform(40.0, 50.0), 2),
            "timestamp": time.time()
        }
        
        client.publish(TOPIC, json.dumps(payload))
        print(f"[Sensor] Published: {payload}")
        
        time.sleep(2)
        
except ConnectionRefusedError:
    print("Error: Could not connect to Mosquitto MQTT broker.")
except KeyboardInterrupt:
    print("\nSimulator stopped by user.")
