import pika
from constants.constants import HOST, PORT, QUEUE_NAME, EXCHANGE_NAME, PRIORITY_QUEUES


class AMQPClient:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.connection = None
        self.channel = None
        self.connect()
        self.setup_queue()

    def connect(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(
            host=HOST,
            port=PORT,
            virtual_host=self.username,
            credentials=credentials
        )
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        print(f"Connected to RabbitMQ broker at {HOST}")

    def setup_queue(self):
        self.channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="direct")
        self.channel.queue_declare(queue=QUEUE_NAME, durable=True)
        self.channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=QUEUE_NAME)
        
        for _, queue_name in PRIORITY_QUEUES.items():
            self.channel.queue_declare(queue=queue_name, durable=True)
            self.channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name, routing_key=queue_name)

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
