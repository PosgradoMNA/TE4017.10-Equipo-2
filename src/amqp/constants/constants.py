HOST = "gorilla-01.lmq.cloudamqp.com"
PORT = 5672
QUEUE_NAME = "amqp_activity_queue"
EXCHANGE_NAME = "amqp_activity_exchange"

PRIORITY_QUEUES = {
    "high": "high_priority_queue",
    "medium": "medium_priority_queue",
    "low": "low_priority_queue",
}
