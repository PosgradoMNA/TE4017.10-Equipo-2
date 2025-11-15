from client.amqp_client import AMQPClient
from constants.constants import EXCHANGE_NAME, QUEUE_NAME, PRIORITY_QUEUES
import pika


class Producer(AMQPClient):
    def publish(self, message, priority="medium"):
        if priority and priority in PRIORITY_QUEUES:
            queue = PRIORITY_QUEUES[priority]
            print(f"Sending message to {priority} priority queue: {message}")
        else:
            queue = QUEUE_NAME
            print(f"Sending message to default queue: {message}")

        self.channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=queue,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print(f"Message sent to queue: {queue}")
        self.close()
