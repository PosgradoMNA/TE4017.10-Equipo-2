from client.mqtt_client import MQTTClient
import sys
from constants.constants import TOPIC
import datetime


class Receiver(MQTTClient):
    def receive(self):
        self.client.on_message = self.on_message
        self.client.subscribe(TOPIC)
        print("Initiating receiver client listening loop...")
        self.client.loop_forever()

    def on_message(self, _client, _userdata, msg):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{timestamp}] Message received:")
        print(f"Payload: {msg.payload.decode()}")
        print(f"Topic: {msg.topic}")
        print(f"QoS: {msg.qos}")
        sys.stdout.flush()
