from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from datetime import datetime, timedelta
import time
import sys
# from json import loads
# import json
import pickle


def cons(request):
    tp = TopicPartition('Ptopic', 0)
    consumer = KafkaConsumer('Ptopic',
                           bootstrap_servers=['localhost:9092'],
                              api_version=(0, 10)

                              ,consumer_timeout_ms=1000
                              )
    consumer.assign([tp])
    consumer.seek_to_beginning(tp)  

# obtain the last offset value
    lastOffset = consumer.end_offsets([tp])[tp]

    for message in consumer:
        print ("Offset:", message.offset)
        print ("Value:", message.message.value)
        if message.offset == lastOffset - 1:
            break 
    # client = "localhost:9092"
    # tp = TopicPartition('Ptopic',0)
             

    # consumer = KafkaConsumer('Ptopic',
    #                        bootstrap_servers=['localhost:9092'],
    #                           api_version=(0, 10)

    #                           ,consumer_timeout_ms=1000
    #                           )
               
    # set1=consumer.assignment()  
    # print(set1)                        
    # # topic = 'Ptopic'
    # # tp = TopicPartition('Ptopic',0)
    # #register to the topic
    # # consumer.assign([tp])

    # # obtain the last offset value
    # consumer.seek_to_end(tp)
    # lastOffset = consumer.position(tp)

    # consumer.seek_to_beginning(tp)        

    # for message in consumer:
    #     print ("Offset:"), message.offset
    #     print ("Value:"), message.message.value
    #     if message.offset == lastOffset - 1:
    #         break
    # consumer = KafkaConsumer('Ptopic',
    #                          bootstrap_servers=['localhost:9092'],
    #                          api_version=(0, 10)

    #                          # ,consumer_timeout_ms=1000
    #                          )
    # tp = TopicPartition('Ptopic', 0)
    # records = consumer.poll(timeout_ms=sys.maxsize)
    # for record in records[tp]:
    #     print(record)
    # try:
    #     while True:
    #         ConsumerRecords < String, String > records = consumer.poll(100)
    #         for ConsumerRecord < String, String > record: records:
    #             log.debug("topic = %s, partition = %d, offset = %d,"
    #                       customer=% s, country = % s"\n", record.topic(), record.partition(), record.offset(),
    #                       record.key(), record.value())

    #             int updatedCount = 1
    #             if (custCountryMap.countainsKey(record.value())):
    #                 updatedCount = custCountryMap.get(record.value()) + 1
    #                 custCountryMap.put(record.value(), updatedCount)

    #                 JSONObject json = new JSONObject(custCountryMap)
    #                 System.out.println(json.toString(4))

    # finally :
    #     consumer.close()
        


def procons(request):
    # producer = KafkaProducer(bootstrap_servers='localhost:9092')

    # stopWriting = datetime.now() + timedelta(seconds=10)
    # while datetime.now() < stopWriting:
    #     producer.send(topic='Ptopic', value=str(
    #         datetime.now()).encode('utf-8'))
    #     time.sleep(1)
    # producer.close()
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                             group_id='my-group', enable_auto_commit=False)
    tp = TopicPartition('Ptopic', 0)
    consumer.assign([tp])
    consumer.seek_to_end(tp)
    last_offset = consumer.position(tp)

    # consumer.seek(tp, last_offset)

# #looping through the consumer
#      for msg in consumer:
#       print(msg)

# # or looping through the polled messages
#       for msg in consumer.poll():
#         print(msg)

    records = consumer.poll(timeout_ms=sys.maxsize)
    for record in records[tp]:
        print(record)
