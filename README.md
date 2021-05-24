# Fraud Stream-detection
Sample fraud detection app using Python and Kafka with Docker for service management

# Setup
Spin the Kafka cluster
``` 
docker-compose -f docker-compose.kafka.yml up
```
Spin the app cluster that contains both generator and detector

` docker-compose up`

## Check Kafka Topic
Use the below command to check the messages being published to a certain topic
```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic queueing.transactions --from-beginning
```
## Inspect different topics

## Fraud topic

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud
```

## legit topic

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit
```

# Tear down
To bring down kafka cluster `docker-compose -d docker-compose.kafka.yml down`

To bring down project 

`docker-compose down` 

To remove project network

`docker network rm kafka-network` 