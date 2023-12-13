from kafka import KafkaConsumer
from lib import Producer, Bmkg

if(__name__ == '__main__'):
    consumer: KafkaConsumer = KafkaConsumer('provinsi', bootstrap_servers=['0.0.0.0:9092'])
    bmkg: Bmkg = Bmkg()

    for message in consumer:
        provinsi: str = message.value.decode('utf-8').strip("'\"")
        producer: Producer = Producer('provinsi_json', '0.0.0.0:9092')

        producer.send(bmkg.execute(provinsi))