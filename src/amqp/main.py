import argparse
from client.producer.producer import Producer
from client.consumer.consumer import Consumer


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--username", type=str, required=True, help="CloudAMQP username"
    )
    parser.add_argument(
        "--password", type=str, required=True, help="CloudAMQP password"
    )
    parser.add_argument(
        "--client-type",
        type=str,
        required=True,
        choices=["consumer", "producer"],
        help="Type of client to execute",
    )
    parser.add_argument(
        "--message",
        type=str,
        required=False,
        help="Message to send via AMQP producer",
    )
    parser.add_argument(
        "--priority",
        type=str,
        required=False,
        choices=["high", "medium", "low"],
        default="medium",
        help="Priority level for the message (default: medium)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_arguments()

    if args.client_type == "consumer":
        consumer = Consumer(args.username, args.password)
        consumer.consume()
    elif args.client_type == "producer":
        if not args.message:
            print("Error: --message is required for producer")
            exit(1)
        producer = Producer(args.username, args.password)
        producer.publish(args.message, args.priority)
