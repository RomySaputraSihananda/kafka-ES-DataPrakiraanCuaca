from kafka import KafkaProducer
from json import dumps
from time import sleep

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [ %(levelname)s ] :: %(message)s', datefmt="%Y-%m-%dT%H:%M:%S")

class Producer:
    def __init__(self, topic: str, servers: str) -> None:
        self.__kafka_producer = KafkaProducer(bootstrap_servers=[servers], value_serializer=lambda x: dumps(x).encode('utf-8'))
        self.__topic = topic

    def send(self, datas: dict) -> None:
        if(not datas): return
        
        if(isinstance(datas, dict)):
            print(len(datas['data']))
            for data in datas['data']:
                logging.info(f'Send to Kafka {data["kabupaten"]["id_ID"]}')
                self.__kafka_producer.send(topic=self.__topic, value=data)
                sleep(2) 
            return

        self.__kafka_producer.send(topic=self.__topic, value=datas)
        sleep(2)

if(__name__ == '__main__'):
    producer: Producer = Producer('provinsi', '0.0.0.0:9092')
    producer.send('DKIJakarta')