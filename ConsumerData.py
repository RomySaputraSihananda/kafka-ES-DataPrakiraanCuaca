from kafka import KafkaConsumer
from json import loads
from elasticsearch import Elasticsearch
from lib import logging

if(__name__ == '__main__'):
    index = 'cuaca'
    consumer: KafkaConsumer = KafkaConsumer('provinsi_json', bootstrap_servers=['0.0.0.0:9092'])
    client: Elasticsearch = Elasticsearch('http://192.168.20.90:9200')

    if(not client.indices.exists(index=index)): client.indices.create(index=index)

    for i, message in enumerate(consumer):
        provinsi_json: str = loads(message.value.decode('utf-8'))

        [id, kabupaten] = [provinsi_json['id'], provinsi_json['kabupaten']['id_ID']]


        if(not client.exists(index=index, id=id)):
            client.create(index=index, document=provinsi_json, id=id)
            logging.info(f'[CREATE] Send to Elastic {kabupaten}')
            continue
        
        logging.info(f'[UPDATE] Send to Elastic {kabupaten}')
        client.update(index=index, doc=provinsi_json, id=id)
