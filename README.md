# TE4017.10-Equipo-2

## MQTT Client

A simple MQTT publisher and receiver implementation using HiveMQ Cloud for real-time messaging.

### Prerequisites

1. **HiveMQ Cloud Account**: Create a free account at [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/)
2. **Client Credentials**: After creating your cluster, get your:
   - Username.
   - Password.
   - Broker URL.
3. **Update Configuration**: Edit `src/mqtt/constants/constants.py` with your topic and broker.

### How it Works

- **Receiver**: Connects to the MQTT broker and continuously listens for incoming messages on a specific topic. It will display all received messages with timestamps and connection details.
- **Publisher**: Connects to the MQTT broker, sends a single message to the specified topic, then disconnects.

Both clients connect to the same HiveMQ Cloud broker and communicate through the configured topic.

### Usage

**Start Receiver (run this first):**
```bash
python3 src/mqtt/main.py --username "your_username" --password "your_password" --client-type receiver
```
The receiver will start listening and wait indefinitely for messages. Keep this terminal open.

**Send Message (run this in another terminal):**
```bash
python3 src/mqtt/main.py --username "your_username" --password "your_password" --client-type publisher --message "Hello World"
```
The publisher sends the message and exits. You should see the message appear in the receiver terminal.

### Requirements
```bash
pip install -r requirements.txt
```

### Structure
```
src/mqtt/
├── main.py
├── client/
│   ├── mqtt_client.py
│   ├── publisher/publisher.py
│   └── receiver/receiver.py
└── constants/constants.py
```
