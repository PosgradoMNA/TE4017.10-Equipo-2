import argparse

from client.publisher.publisher import Publisher
from client.receiver.receiver import Receiver


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=True, help="HiveMQ username")
    parser.add_argument("--password", type=str, required=True, help="HiveMQ password")
    parser.add_argument(
        "--client-type",
        type=str,
        required=True,
        choices=["receiver", "publisher"],
        help="Type of the client to execute",
    )
    parser.add_argument(
        "--payload",
        type=str,
        required=False,
        help="Message to send via HiveMQ client for the publisher client type",
    )

    args = parser.parse_args()

    return args.username, args.password, args.client_type, args.payload


if __name__ == "__main__":
    username, password, client_type, payload = get_arguments()
    if client_type == "receiver":
        receiver = Receiver(username, password)
        receiver.receive()
    elif client_type == "publisher":
        publisher = Publisher(username, password)
        publisher.publish(payload)
