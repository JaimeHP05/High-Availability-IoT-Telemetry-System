# High Availability IoT Telemetry System

This repository contains the source code and documentation for the joint final project of the Virtualization Systems and NoSQL Databases modules.

## Project Overview
The project demonstrates a fault-tolerant, highly available infrastructure for IoT data ingestion. It relies on a distributed MongoDB Replica Set hosted on independent LXD containers, communicating across statically routed subnets, and utilizing a shared NFS storage backend to ensure data survival during node failures.

## Repository Contents
* `Project-Report.pdf`: Comprehensive technical report detailing the infrastructure setup, database configuration, and disaster recovery testing.
* `sensor.py`: Python script utilizing the `paho-mqtt` library to simulate an edge IoT device publishing temperature and humidity telemetry.
* `ingest.py`: Python daemon that subscribes to the MQTT broker and inserts the incoming JSON payloads into the MongoDB Replica Set via `pymongo`.

## Requirements
* Python 3.x
* Mosquitto MQTT Broker
* MongoDB 7.0 (Configured as a Replica Set)
* `pip install paho-mqtt pymongo`
