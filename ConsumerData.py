import os
from kafka import KafkaConsumer
from json import dumps, loads

if(__name__ == '__main__'):
    consumer: KafkaConsumer = KafkaConsumer('provinsi_json', bootstrap_servers=['0.0.0.0:9092'])

    for message in consumer:
        provinsi_json: str = loads(message.value.decode('utf-8'))

        output = f'data'

        if(not os.path.exists(output)):
                os.makedirs(output)

        with open(f'{output}/{provinsi_json["kabupaten"]["id_ID"]}.json', 'w') as file:
            file.write(dumps(provinsi_json, indent=2))