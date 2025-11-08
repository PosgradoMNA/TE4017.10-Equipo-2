import uuid
import paho.mqtt.client as paho
import ssl
from constants.constants import BROKER, PORT


class MQTTClient:
    def __init__(self, username: str, password: str):
        self.connected = False
        self.client = self.create_client(username, password)
        self.client.connect(BROKER, PORT)

    def create_client(self, username: str, password: str):
        client_id = uuid.uuid4()
        client = paho.Client(protocol=paho.MQTTv5, userdata=client_id)
        client.tls_set(tls_version=ssl.PROTOCOL_TLS)
        client.username_pw_set(username, password)
        client.on_connect = self.on_connect
        return client

    def on_connect(self, _client, userdata, _flags, result_code, _properties):
        print(f"\nConnected with result code {result_code} for client {userdata}\n")
        self.connected = True
