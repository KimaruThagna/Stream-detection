import os, time, json
from kafka import KafkaProducer
from random import choices, randint
from string import ascii_letters, digits

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


account_chars = digits + ascii_letters


def _random_account_id():
    
    return "".join(choices(account_chars, k=12))


def _random_amount():
    
    return randint(100, 1000000) / 100


def create_random_transaction():
    return {
        "source": _random_account_id(),
        "target": _random_account_id(),
        "amount": _random_amount(),
        "currency": "KES",
    }
    

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                         #json encode all values
                         value_serializer=lambda value: json.dumps(value).encode(),)

while True:
    transaction = create_random_transaction()
    # Kafka messages are sent in bytes
    producer.send(TRANSACTIONS_TOPIC, value=transaction)
    time.sleep(SLEEP_TIME)  