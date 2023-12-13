from kafka import KafkaProducer
from json import dumps
from time import sleep


class Producer:
    def __init__(self, topic: str, servers: list) -> None:
        self.__kafka_producer = KafkaProducer(bootstrap_servers=servers, value_serializer=lambda x: dumps(x).encode('utf-8'))
        self.__topic = topic

    def send(self, data: dict) -> None:
        self.__kafka_producer.send(topic=self.__topic, value=data)
        sleep(3)

        # datas = datas["data"]["result"]
        # for data in datas:
        #     if (data.get("title") == "") or (data.get("content") == ""):
        #         continue
        #     else:
        #         print(data)
        #         self.__kafka_producer.send(topic=self.__topic, value=data)
        #         sleep(5)

if(__name__ == '__main__'):
    producer: Producer = Producer('provinsi', ['0.0.0.0:9092'])
    producer.send('DKIJakarta')