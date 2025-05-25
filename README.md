# progjar-2
Tugas 2 Pemrograman Jaringan (D) 2025 adalah implementasi **Time Server** berbasis **TCP socket** menggunakan **Python**, yang mampu menangani banyak klien secara **concurrent** menggunakan **multithreading**. Server akan merespons permintaan waktu dari klien dalam format yang telah ditentukan.



## Fitur

- Server TCP multithreaded
- Melayani banyak klien secara bersamaan
- Respon waktu akurat dalam format 24 jam
- Kompatibel dengan klien di jaringan lokal



## Cara Menjalankan

### 1. Jalankan server di mesin-1
```bash
python3 time_server.py
```

### 2. Jalankan client di mesin-2 dan mesin-3
```bash
python3 run_time_client_at.py
```

Perintah ini akan otomatis menjalankan `time_client.py` sesuai waktu yang ditentukan di dalam script `run_time_client_at.py`. Anda dapat mengganti waktu ini sesuai keinginan Anda.



## Format Protokol

- Permintaan dari client:
  - `"TIME\r\n"` : Meminta waktu dari server
  - `"QUIT\r\n"` : Mengakhiri koneksi
- Balasan dari server:
  - `"JAM hh:mm:ss\r\n"` : Format respons waktu saat ini



## Pengujian
Pengujian dilakukan dari dua mesin (172.16.16.102 dan 172.16.16.103) yang mengirimkan total 10 request secara concurrent. Server berhasil merespons semua permintaan tanpa error, membuktikan kestabilan arsitektur multithreaded.
