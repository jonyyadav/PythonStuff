from django.shortcuts import render
from kafka import KafkaProducer
# from json import loads
# import json
import pickle
from django.http import HttpResponse

# Create your views here.
def kfk(request):   
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    v = {
        'msg': {
            'hello': 'world',
        },
    }
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    print(serialized_data)
    producer.send('Ptopic', serialized_data)
    
    return HttpResponse(200)
