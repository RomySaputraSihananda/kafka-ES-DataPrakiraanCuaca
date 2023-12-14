from argparse import ArgumentParser;
from lib import ConsumerData

if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--topic", '-t', type=str, default='provinsi_json')
    argp.add_argument("--server_k", '-sk', type=str, default='0.0.0.0:9092')
    argp.add_argument("--index", '-i', type=str, default='cuaca')
    argp.add_argument("--server_es", '-se', type=str, default='0.0.0.0:9200')
    args = argp.parse_args()

    print(args.topic)

    consumer_json: ConsumerData = ConsumerData(index_elasticsearch=args.index,  server_elasticsearch=f'http://{args.server_es}', topik_kafka=args.topic, server_kafka=args.server_k)
    consumer_json.excecute()