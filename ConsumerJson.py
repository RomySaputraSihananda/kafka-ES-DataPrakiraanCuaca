from lib import ConsumerData

if(__name__ == '__main__'):
    
    consumer_json: ConsumerData = ConsumerData('cuaca',  'http://192.168.20.90:9200', 'provinsi_json', '0.0.0.0:9092')
    consumer_json.excecute()