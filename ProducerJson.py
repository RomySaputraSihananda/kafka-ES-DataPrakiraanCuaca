from lib import ProducerData

if(__name__ == '__main__'):
    produser_json: ProducerData = ProducerData('provinsi_json', '0.0.0.0:9092')
    produser_json.excecute('Lampung')