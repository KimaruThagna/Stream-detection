import os, time, json
from kafka import KafkaProducer

from transactions import create_random_transaction

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)

while True:
    transaction = create_random_transaction()
    message = json.dumps(transaction)
    # Kafka messages are sent in bytes
    producer.send("queueing.transactions", value=message.encode())
    time.sleep(1)  