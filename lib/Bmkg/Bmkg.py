import requests
import xmltodict

from requests import Response
from json import dumps
from datetime import datetime

from Bmkg.helpers import Kode_Parameter, Kode_Cuaca, Kode_Arah_Angin

class Bmkg:
    def __init__(self) -> None:
        self.__BASE_URL: str = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/'
        self.__result: dict = {}
        self.__result['timestamp']: str = None
        self.__result['source']: str = None
        self.__result['productioncenter']: str = None
        self.__result['data']: list = []

    def __str_2_datetime(self, text: str) -> str:
        return datetime.strptime(text, "%Y%m%d%H%M%S").strftime("%Y-%m-%dT%H:%M:%S");

    def __str_2_number(self, text: str):
        try:
            return float(text)
        except:
            return Kode_Arah_Angin[text]
            
    def __filter_area(self, areas: list) -> None:
        for area in areas:
            self.__result['data'].append({
                "kabupaten": {name['@xml:lang'] : name['#text'] for name in area['name']},
                "provinsi": area['@domain'],
                "coordinate": area['@coordinate'],
                "parameter":{
                    Kode_Parameter[parameter["@id"]]: {
                        "type": parameter['@type'],
                        "timerange": [
                            {
                                "datetime": self.__str_2_datetime(timerange['@datetime']),
                                "value": {
                                    item['@unit']: self.__str_2_number(item['#text']) if isinstance(item, dict) else item
                                    for item in timerange['value']
                                } if isinstance(timerange['value'], list) else {
                                    timerange['value']['@unit']: self.__str_2_number(timerange['value']['#text'] )
                                } if timerange['value']['@unit'] != 'icon' else Kode_Cuaca[timerange['value']['#text']]
                            } for timerange in parameter['timerange']
                        ]
                    } for parameter in area['parameter']
                }
            })

    def execute(self, provinsi: str) -> str:
        url = self.__BASE_URL + f"DigitalForecast-{provinsi}.xml"
        res: Response = requests.get(url)

        if(res.status_code != 200): return

        data = xmltodict.parse(res.content.decode('utf-8'))

        self.__result['timestamp']: str = self.__str_2_datetime(data['data']['forecast']['issue']['timestamp'])
        self.__result['source']: str = data['data']['@source']
        self.__result['productioncenter']: str = data['data']['@productioncenter']

        self.__filter_area(data['data']['forecast']['area'])

        return self.__result

# testing
if(__name__ == "__main__"):
    bmkg: Bmkg = Bmkg()

    with open('test_data.json', 'w') as file:
        file.write(dumps(bmkg.execute('Banteng'), indent=2))
    # print(bmkg.execute('Aceh'))