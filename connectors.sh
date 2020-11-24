#!/bin/bash

# https://debezium.io/documentation/reference/1.3/connectors/mysql.html#mysql-connector-configuration-properties_debezium
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d'
{
  "name": "inventory-connector",  
  "config": {  
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "tasks.max": "1",  
    "database.hostname": "mysql",  
    "database.port": "3306",
    "database.user": "root",
    "database.password": "mysqlpass",
    "database.server.id": "184054",  
    "database.server.name": "dbserver1",  
    "database.include.list": "inventory",  
    "database.history.kafka.bootstrap.servers": "kafka-1:9092",  
    "database.history.kafka.topic": "schema-changes.inventory",
    "database.allowPublicKeyRetrieval": "true" 
  }
}'

curl -i -X GET -H "Accept:application/json" localhost:8083/connectors/inventory-connector