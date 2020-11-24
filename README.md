# docker-compose-kafka-zookeeper


## Create stack

```
docker-compose up -d
```

## Load data

```
docker-compose exec mysql bash
root@d48eb720ebe6:/# mysql -u debezium -p'debeziumpass' communication < /data/scripts/schema-setup.sql
```

## Create MySQL/Kafka connector

```
curl -s -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d'
{
  "name": "communication-connector",  
  "config": {  
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "tasks.max": "1",  
    "database.hostname": "mysql",  
    "database.port": "3306",
    "database.user": "root",
    "database.password": "mysqlpass",
    "database.server.id": "184054",  
    "database.server.name": "dbserver1",  
    "database.include.list": "communication",  
    "database.history.kafka.bootstrap.servers": "kafka-1:9092,kafka-2:9092,kafka-3:9092",  
    "database.history.kafka.topic": "schema-changes.communication",
    "database.allowPublicKeyRetrieval": "true" 
  }
}'
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