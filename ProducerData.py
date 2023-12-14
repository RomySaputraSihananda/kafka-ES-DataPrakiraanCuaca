from kafka import KafkaConsumer
from lib import Producer, Bmkg
from lib import logging

if(__name__ == '__main__'):
    consumer: KafkaConsumer = KafkaConsumer('provinsi', bootstrap_servers=['0.0.0.0:9092'])

    for message in consumer:
        provinsi: str = message.value.decode('utf-8').strip("'\"")
        producer: Producer = Producer('provinsi_json', '0.0.0.0:9092')

        bmkg: Bmkg = Bmkg()

        logging.info(f'[UPDATE] Send to Kafka {provinsi}')
        producer.send(bmkg.execute(provinsi))