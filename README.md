# TE4017.10-Equipo-2

## MQTT Client

A simple MQTT publisher and receiver implementation using HiveMQ Cloud for real-time messaging.

## AMQP Client

A simple AMQP producer and consumer implementation using CloudAMQP (RabbitMQ) for message queuing.

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
python3 src/mqtt/main.py --username "your_username" --password "your_password" --client-type publisher --payload "Hello World"
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

## AMQP Usage

### Prerequisites

1. **CloudAMQP Account**: Create a free account at [CloudAMQP](https://www.cloudamqp.com/)
2. **Instance Setup**: Create a RabbitMQ instance and get your username and password
3. **Update Configuration**: Edit `src/amqp/constants/constants.py` with your host, queue and exchange names

### How it Works

- **Consumer**: Connects to RabbitMQ and listens to priority queues with hierarchy (HIGH > MEDIUM > LOW)
- **Producer**: Connects to RabbitMQ and sends messages to specific priority queues
- **Priority System**: High priority messages get processed faster with higher prefetch counts

### Usage

**Start Consumer (run this first):**
```bash
python3 src/amqp/main.py --username "your_username" --password "your_password" --client-type consumer
```

**Send Messages with Priority:**
```bash
# High priority message
python3 src/amqp/main.py --username "your_username" --password "your_password" --client-type producer --message "Urgent task" --priority high

# Medium priority message (default)
python3 src/amqp/main.py --username "your_username" --password "your_password" --client-type producer --message "Normal task"

# Low priority message
python3 src/amqp/main.py --username "your_username" --password "your_password" --client-type producer --message "Background task" --priority low
```

### Structure
```
src/amqp/
├── main.py
├── client/
│   ├── amqp_client.py
│   ├── producer/producer.py
│   └── consumer/consumer.py
└── constants/constants.py
```
