from argparse import ArgumentParser;
from lib import ConsumerData

if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--topic", '-t', type=str, default='DKIJakarta')
    argp.add_argument("--server_k", '-sk', type=str)
    argp.add_argument("--document", '-d', type=str)
    argp.add_argument("--server_es", '-se', type=str)
    args = argp.parse_args()

    consumer_json: ConsumerData = ConsumerData('cuaca',  'http://192.168.20.90:9200', 'provinsi_json', '0.0.0.0:9092')
    consumer_json.excecute()