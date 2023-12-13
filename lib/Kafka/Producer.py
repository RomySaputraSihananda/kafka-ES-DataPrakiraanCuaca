from kafka import KafkaProducer
from json import dumps
from time import sleep


class Producer:
    def __init__(self, topic: str, servers: str) -> None:
        self.__kafka_producer = KafkaProducer(bootstrap_servers=[servers], value_serializer=lambda x: dumps(x).encode('utf-8'))
        self.__topic = topic

    def send(self, datas: dict) -> None:
        if(not datas): return
        if(isinstance(datas, dict)):
            for data in datas['data']: self.__kafka_producer.send(topic=self.__topic, value=data)

        self.__kafka_producer.send(topic=self.__topic, value=datas)
        sleep(2)

if(__name__ == '__main__'):
    producer: Producer = Producer('provinsi', '0.0.0.0:9092')
    producer.send('DKIJakarta')