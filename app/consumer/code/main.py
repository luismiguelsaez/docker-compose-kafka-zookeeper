from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
            'numtest',
            bootstrap_servers=['kafka-1:9092','kafka-2:9092','kafka-3:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
           )

for message in consumer:
    print(message.value)
