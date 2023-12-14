[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# kafka-ES-DataPrakiraanCuaca

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GBTKs-HakAAZd50.jpeg)

Aplikasi ini dibuat untuk mensimulasikan transmisi data hasil crawling dari [DataPrakiraanCuaca](https://github.com/RomySaputraSihananda/craw-DataPrakiraanCuaca) menggunakan Python, Kafka, dan Elasticsearch.

## Requirements

- **Python >= 3.11.4**
- **Requests >= 2.31.0**
- **xmltodict >= 0.12.0**
- **elasticsearch >= 8.10.0**
- **kafka_python >= 2.0.2**

## File structure

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/flowkafespy.png)

| File            |                                                                   Description                                                                   |
| --------------- | :---------------------------------------------------------------------------------------------------------------------------------------------: |
| ProducerJson.py | Berfungsi mengambil data provinsi diteruskan ke engine yang menghasilkan data JSON. Juga, berfungsi sebagai producer untuk topic provinsi_json. |
| ConsumerJson.py |                      Consumer dari topic provinsi_json. Data ini kemudian dikirim ke Elasticsearch sebagai sebuah dokumen.                      |

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/kafka-ES-DataPrakiraanCuaca

# Change Directory
cd kafka-ES-DataPrakiraanCuaca

# Install Requirement
pip install -r requirements.txt
```

## Example Usage

### Start Consumer of Kafka

```bash

```

### Start Producer of Kafka

```bash

```

## License

This project is licensed under the [MIT License](LICENSE).
