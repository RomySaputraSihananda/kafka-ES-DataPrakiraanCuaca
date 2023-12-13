from lib import Producer

if(__name__ == '__main__'):
    producer: Producer = Producer('provinsi', '0.0.0.0:9092')
    while(True):
        provinsi = input('provinsi: ')
        producer.send(provinsi)
