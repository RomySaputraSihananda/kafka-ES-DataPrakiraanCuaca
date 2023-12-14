from kafka import KafkaConsumer
from lib import Producer, Bmkg

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [ %(levelname)s ] :: %(message)s', datefmt="%Y-%m-%dT%H:%M:%S")

class ProducerData:
    def __init__(self, topik_kafka: str, server_kafka: str):
        self.__producer: Producer = Producer(topik_kafka, server_kafka)
        self.__bmkg: Bmkg = Bmkg()

    def excecute(self, provinsi: str):
        logging.info(f'[UPDATE] Send to Kafka {provinsi} json')
        self.__producer.send(self.__bmkg.execute(provinsi))

# testing
if(__name__ == '__main__'):
    # for message in consumer:
    #     provinsi: str = message.value.decode('utf-8').strip("'\"")
    produser_json: ProducerData = ProducerData('provinsi_json', '0.0.0.0:9092')
    produser_json.excecute()

