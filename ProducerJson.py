from argparse import ArgumentParser;
from lib import ProducerData

if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--provinsi", '-p', type=str, default='DKIJakarta')
    argp.add_argument("--topic", '-t', type=str, default='provinsi_json')
    argp.add_argument("--server_k", '-sk', type=str, default='0.0.0.0:9092')
    args = argp.parse_args()
    
    produser_json: ProducerData = ProducerData(topik_kafka=args.topic, server_kafka=args.server_k)
    produser_json.excecute(args.provinsi)