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

## Struktur File

1. User.py
   - Deskripsi: Mengambil input dari pengguna dan berfungsi sebagai producer untuk topic provinsi.
2. ProducerJson.py
   - Deskripsi: Menjadi consumer untuk topic provinsi. Data dari provinsi diteruskan ke engine yang menghasilkan data JSON. Juga, berfungsi sebagai producer untuk topic provinsi_json.
3. ConsumerJson.py
   - Deskripsi: Consumer dari topic provinsi_json. Data ini kemudian dikirim ke Elasticsearch sebagai sebuah dokumen.

## Langkah-langkah Penggunaan

1. Jalankan User.py untuk mengambil input dari pengguna.
2. Jalankan ProducerData.py untuk memulai transmisi data dari provinsi.
3. ConsumerData.py akan menjalankan proses konsumsi dan mengirimkan data ke Elasticsearch.

Pastikan Anda telah menginstal dependensi yang diperlukan sebelum menjalankan aplikasi ini.
