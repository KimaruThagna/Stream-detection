import os, time, json
from kafka import KafkaProducer

from generator.transactions import create_random_transaction

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                         #json encode all values
                         value_serializer=lambda value: json.dumps(value).encode(),)

while True:
    transaction = create_random_transaction()
    # Kafka messages are sent in bytes
    producer.send(TRANSACTIONS_TOPIC, value=transaction)
    time.sleep(SLEEP_TIME)  