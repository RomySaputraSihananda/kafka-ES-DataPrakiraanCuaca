# kafka-ES-DataPrakiraanCuaca

Aplikasi ini dibuat untuk mensimulasikan transmisi data menggunakan Python, Kafka, dan Elasticsearch.

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
