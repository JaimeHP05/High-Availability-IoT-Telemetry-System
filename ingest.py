import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json

BROKER = "localhost"
TOPIC = "telemetry/environmental"

MONGO_URI = "mongodb://10.37.37.29:27017,10.159.75.192:27017,10.159.75.21:27017/?replicaSet=rs0"

try:
    db_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = db_client["iot_telemetry"]
    collection = db["sensors"]
    print("Connected to MongoDB Replica Set successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"[Ingestor] Received data from: {payload.get('sensor_id')}")
        
        collection.insert_one(payload)
        print(" -> Saved to MongoDB.")
    except Exception as e:
        print(f"Error processing message: {e}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

print("Starting Ingestion Daemon...")
mqtt_client.connect(BROKER, 1883, 60)
mqtt_client.loop_forever()
