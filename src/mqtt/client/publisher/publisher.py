from client.mqtt_client import MQTTClient
from constants.constants import QOS, TOPIC


class Publisher(MQTTClient):
    def publish(self, payload):
        self.client.loop_start()
        while not self.connected:
            pass
        print("Sending payload:", payload)
        self.client.publish(TOPIC, payload, qos=QOS)
        self.client.loop_stop()
        self.client.disconnect()
