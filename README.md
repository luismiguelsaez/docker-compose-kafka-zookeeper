# docker-compose-kafka-zookeeper


## Create stack

```
docker-compose up -d
```

## Load data

```
docker-compose exec mysql bash
root@d48eb720ebe6:/# mysql -u debezium -p'debeziumpass' communication < /app/setup/sql/schema-setup.sql
```

## Create MySQL/Kafka connector

```
curl -s -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ --data-binary "@app/setup/api/connector.json"
```

```
curl -s -X GET -H "Accept:application/json" localhost:8083/connectors/communication-connector
```

## List topics and events

```
docker-compose exec kafka-1 kafka-topics --list --zookeeper zookeeper-1:2181,zookeeper-2:2181,zookeeper-3,2181
docker-compose exec kafka-1 kafka-topics --describe --topic dbserver1.communication.messages --zookeeper zookeeper-1:2181,zookeeper-2:2181,zookeeper-3,2181
docker-compose exec kafka-1 kafka-console-consumer --topic dbserver1.communication.messages --from-beginning --bootstrap-server localhost:9092
```