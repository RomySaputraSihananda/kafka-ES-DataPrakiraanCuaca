from kafka import KafkaConsumer
from json import loads
from elasticsearch import Elasticsearch
from lib import logging

class ConsumerJson:
    def __init__(self, index_elasticsearch: str, server_elasticsearch: str, topik_kafka: str, server_kafka: str):
        self.__index_elasticsearch: str = index_elasticsearch
        self.__client_elasticsearch: Elasticsearch = Elasticsearch(server_elasticsearch)
        self.__consumer_kafka: KafkaConsumer = KafkaConsumer(topik_kafka, bootstrap_servers=[server_kafka])

    def excecute(self):
        if(not self.__client_elasticsearch.indices.exists(index=self.__index_elasticsearch)): 
            self.__client_elasticsearch.indices.create(index=self.__index_elasticsearch)

        for message in self.__consumer_kafka:
            provinsi_json: str = loads(message.value.decode('utf-8'))

            [id, kabupaten] = [provinsi_json['id'], provinsi_json['kabupaten']['id_ID']]

            if(not self.__client_elasticsearch.exists(index=self.__index_elasticsearch, id=id)):
                self.__client_elasticsearch.create(index=self.__index_elasticsearch, document=provinsi_json, id=id)
                logging.info(f'[CREATE] Send to Elastic {kabupaten}')
                continue

            logging.info(f'[UPDATE] Send to Elastic {kabupaten}')
            self.__client_elasticsearch.update(index=self.__index_elasticsearch, doc=provinsi_json, id=id)

if(__name__ == '__main__'):
    consumer_json: ConsumerJson = ConsumerJson('http://192.168.20.90:9200', 'cuaca', 'provinsi_json', '0.0.0.0:9092')
    consumer_json.excecute()

