from utils.timestamp_utils import generate_timestamp
from client.amqp_client import AMQPClient
from constants.constants import PRIORITY_QUEUES


class Consumer(AMQPClient):
    def consume(self):
        self.channel.basic_qos(prefetch_count=10)
        self.channel.basic_consume(
            queue=PRIORITY_QUEUES["high"], on_message_callback=self.on_high_priority
        )

        self.channel.basic_qos(prefetch_count=5)
        self.channel.basic_consume(
            queue=PRIORITY_QUEUES["medium"], on_message_callback=self.on_medium_priority
        )

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=PRIORITY_QUEUES["low"], on_message_callback=self.on_low_priority
        )

        print(
            "Waiting for messages with hierarchy: HIGH (prefetch=10) > MEDIUM (prefetch=5) > LOW (prefetch=1)"
        )
        print("To exit press CTRL+C")

        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
            self.close()

    def on_high_priority(self, channel, method, properties, body):
        print(f"\n[{generate_timestamp()}] HIGH PRIORITY MESSAGE:")
        print(f"Payload: {body.decode()}")
        print(f"Queue: {method.routing_key}")
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def on_medium_priority(self, channel, method, properties, body):
        print(f"\n[{generate_timestamp()}] MEDIUM PRIORITY MESSAGE:")
        print(f"Payload: {body.decode()}")
        print(f"Queue: {method.routing_key}")
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def on_low_priority(self, channel, method, properties, body):
        print(f"\n[{generate_timestamp()}] LOW PRIORITY MESSAGE:")
        print(f"Payload: {body.decode()}")
        print(f"Queue: {method.routing_key}")
        channel.basic_ack(delivery_tag=method.delivery_tag)
