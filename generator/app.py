import os, time
from kafka import KafkaProducer

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)
while True:
    message = ""  # TODO
    # Kafka messages are sent in bytes
    producer.send("queueing.transactions", value=message.encode())
    time.sleep(1)  