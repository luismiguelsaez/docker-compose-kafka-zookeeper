from kafka import KafkaConsumer


kafka_bootstrap_servers = ['kafka-1:9092','kafka-2:9092','kafka-3:9092']
kafka_topic_name = 'dbserver1.communication.messages'

kafka_consumer = KafkaConsumer ( kafka_topic_name, group_id ='group1', bootstrap_servers = kafka_bootstrap_servers )

for msg in kafka_consumer:
    print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
