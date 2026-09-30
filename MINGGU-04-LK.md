# Lembar Kerja Mahasiswa (LK) — Pertemuan 6

## Tugas 4: Dashboard Design (Wireframe & Prototype)

> **PETUNJUK:** Copy ke `kel-XX/minggu-06/LK.md`. Commit min 10x. Screenshot
> wireframe & prototype. Push sebelum akhir sesi.

## Identitas

| Field    | Isi                           |
| -------- | ----------------------------- |
| Kelas    | SI-C                          |
| Kelompok | 06                            |
| Sub-CPMK | Sub-CPMK03 — Dashboard Design |
| Bobot    | 2% (Tugas 4)                  |

## Aktivitas 1 — Audience-Task-Context (1 paragraf)

**Audience:** Dashboard ditujukan kepada pemilik atau pengelola Mie Ayam Afui yang membutuhkan informasi penjualan dari tiga cabang. **Task:** Dashboard digunakan untuk membantu melihat total penjualan, jumlah item terjual, menu terlaris, tren penjualan berdasarkan tanggal, perbandingan penjualan antar-cabang, serta peringkat menu pada setiap cabang sehingga pengelola dapat melakukan evaluasi penjualan dan menentukan menu yang perlu diperhatikan. **Context:** Dashboard digunakan sebagai media analisis setelah data transaksi dari Mie Ayam Afui diproses melalui ETL menggunakan Python dan Pandas, kemudian disimpan pada PostgreSQL Data Warehouse dengan Star Schema. Data yang digunakan berasal dari `fact_penjualan`, `dim_tanggal`, `dim_cabang`, `dim_menu`, dan `dim_porsi`. Hasil analisis `RANK()` dan `PARTITION BY` pada LK 5 juga digunakan sebagai dasar untuk melihat peringkat menu pada masing-masing cabang. Untuk business question mengenai perbandingan channel langsung dan ojek online setelah komisi, belum ditampilkan karena data channel dan biaya komisi belum tersedia pada model data yang digunakan.

## Aktivitas 2 — Wireframe lo-fi

> Tempel foto kertas / link Excalidraw / sketsa ASCII. Sebut alasan per visual.

**Rancangan Dashboard:**

```text
┌─────────────────────────────────────────────────────────────────┐
│             DASHBOARD PENJUALAN MIE AYAM AFUI                  │
├─────────────────────────────────────────────────────────────────┤
│ Filter Tanggal       Filter Cabang       Filter Menu             │
│     [▼]                  [▼]                  [▼]               │
├──────────────────┬──────────────────┬───────────────────────────┤
│ TOTAL PENJUALAN  │ TOTAL ITEM       │ MENU TERLARIS             │
│ Rp ...           │ ... item         │ ...                       │
├──────────────────┴──────────────────┴───────────────────────────┤
│                                                                 │
│                    TREN PENJUALAN                               │
│                                                                 │
│                       Line Chart                                │
│                                                                 │
├────────────────────────────────┬────────────────────────────────┤
│ PENJUALAN PER CABANG            │ TOP MENU                       │
│                                │                                │
│ Bar Chart                      │ Bar Chart                      │
│                                │                                │
└────────────────────────────────┴────────────────────────────────┘
```

**Alasan visual:**

* **KPI Card — Total Penjualan:** digunakan untuk menampilkan nilai total penjualan secara ringkas sehingga pengguna dapat langsung mengetahui nilai penjualan keseluruhan.
* **KPI Card — Total Item Terjual:** digunakan untuk mengetahui jumlah seluruh item yang terjual dari data transaksi.
* **KPI Card — Menu Terlaris:** digunakan untuk menunjukkan menu dengan jumlah item terjual paling tinggi.
* **Line Chart — Tren Penjualan:** digunakan untuk melihat perubahan total penjualan berdasarkan tanggal sehingga pola penjualan dapat diamati.
* **Bar Chart — Penjualan per Cabang:** digunakan untuk membandingkan total penjualan dari tiga cabang Mie Ayam Afui.
* **Bar Chart — Top Menu:** digunakan untuk mengetahui menu dengan jumlah item terjual paling tinggi dan mendukung hasil analisis ranking menu dari LK 5.
* **Slicer Tanggal:** digunakan untuk membatasi data berdasarkan periode tertentu.
* **Slicer Cabang:** digunakan untuk melihat data dari cabang tertentu.
* **Slicer Menu:** digunakan untuk melihat performa menu tertentu.

## Aktivitas 3 — Prototype hi-fi Power BI

> Screenshot dashboard (min. 3 visual + 1 slicer). `.pbix` opsional commit.

**Daftar visual:**

* **KPI Card Total Penjualan** — menjawab pertanyaan mengenai berapa total nilai penjualan Mie Ayam Afui pada periode yang dipilih.
* **KPI Card Total Item Terjual** — menjawab pertanyaan mengenai berapa banyak item yang berhasil terjual.
* **KPI Card Menu Terlaris** — menjawab pertanyaan mengenai menu apa yang memiliki jumlah item terjual paling tinggi.
* **Line Chart Tren Penjualan** — menjawab pertanyaan mengenai bagaimana perubahan penjualan berdasarkan tanggal.
* **Bar Chart Penjualan per Cabang** — menjawab pertanyaan mengenai bagaimana perbandingan penjualan antara tiga cabang Mie Ayam Afui.
* **Bar Chart Top Menu** — menjawab pertanyaan mengenai menu apa yang paling banyak terjual dan bagaimana peringkat menu berdasarkan jumlah item terjual.
* **Slicer: Tanggal** — digunakan untuk memfilter dashboard berdasarkan periode tanggal.
* **Slicer: Cabang** — digunakan untuk memfilter dashboard berdasarkan cabang.
* **Slicer: Menu** — digunakan untuk memfilter dashboard berdasarkan menu.

**Screenshot dashboard Power BI:**
`[Tempel screenshot prototype Power BI di sini]`

## Aktivitas 4 — Peer Review (feedback ke 1 kelompok lain)

* Kelompok yang direview: `<kel-YY>`
* Feedback (clarity / visual / audience-fit): Dashboard kelompok yang direview sudah memiliki informasi utama yang dapat membantu pengguna memahami kondisi data. Visual yang digunakan cukup sesuai dengan kebutuhan analisis, tetapi penempatan dan ukuran visual perlu dibuat lebih konsisten agar informasi utama dapat ditemukan dengan lebih mudah. Penggunaan filter juga perlu dibuat jelas agar pengguna memahami data yang sedang ditampilkan.

## Refleksi

* Perubahan desain dari wireframe → prototype berdasarkan feedback: Setelah mendapatkan feedback, desain dashboard disesuaikan dengan memperjelas posisi KPI dan mengatur ukuran visual agar informasi utama lebih mudah terlihat. Grafik juga ditata agar hubungan antarinformasi lebih mudah dipahami. Slicer ditempatkan pada bagian atas dashboard sehingga pengguna dapat melakukan filter berdasarkan tanggal, cabang, dan menu dengan lebih mudah. Penyesuaian tersebut tetap mempertahankan visual utama yang telah dirancang pada wireframe karena visual tersebut sudah sesuai dengan business question dan data yang tersedia.

### [Isyaka Dhafa Maulana — Ketua]

Pada pertemuan ini saya mempelajari bahwa dashboard BI tidak hanya berisi kumpulan grafik, tetapi harus dibuat berdasarkan kebutuhan pengguna dan business question. Dalam kasus Mie Ayam Afui, saya menghubungkan hasil dari LK sebelumnya, mulai dari Star Schema, proses ETL, sampai query `RANK()` pada LK 5 untuk menentukan informasi yang perlu ditampilkan pada dashboard.

Saya juga belajar bahwa wireframe membantu menentukan susunan dashboard sebelum dibuat pada Power BI. Setelah menjadi prototype, saya memahami bahwa ukuran, posisi, dan pemilihan visual perlu diperhatikan agar informasi seperti total penjualan, jumlah item terjual, menu terlaris, dan performa cabang dapat dipahami dengan cepat.

### [Habrian Daffa Dwiyandana - Anggota 2]

Pada pertemuan ini saya belajar bahwa desain dashboard harus disesuaikan dengan kebutuhan pengguna dan tidak hanya berfokus pada jumlah grafik. Setiap visual harus memiliki tujuan yang jelas dan dapat membantu menjawab business question yang telah ditentukan pada tugas sebelumnya.

Saya juga memahami hubungan antara hasil query SQL pada LK 5 dengan visualisasi pada Power BI. Query `RANK()` dengan `PARTITION BY` dapat digunakan untuk mengetahui peringkat menu pada setiap cabang dan hasil tersebut dapat menjadi dasar dalam menentukan visual Top Menu pada dashboard.

### [Mohamad Safi'i - Anggota 3]

Pada tugas ini saya memahami bahwa dashboard merupakan bagian lanjutan dari proses BI yang telah dilakukan pada pertemuan sebelumnya. Data dari `fact_penjualan` dan tabel dimensi dapat digunakan untuk menghasilkan informasi yang lebih mudah dipahami melalui KPI dan grafik.

Saya juga belajar bahwa kebutuhan analisis harus disesuaikan dengan ketersediaan data. Business question mengenai channel penjualan langsung dan ojek online memang sudah ditentukan sebelumnya, tetapi data channel dan biaya komisi belum terdapat dalam model data yang digunakan sehingga belum dapat ditampilkan pada prototype dashboard.

### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]

Pada pertemuan ini saya belajar membuat wireframe sebelum membuat prototype dashboard pada Power BI. Dengan wireframe, kami dapat menentukan posisi KPI, grafik, dan filter terlebih dahulu sehingga dashboard memiliki susunan yang lebih terarah.

Saya juga memahami bahwa pemilihan visual harus disesuaikan dengan jenis informasi yang ingin ditampilkan. Line chart digunakan untuk melihat tren penjualan berdasarkan tanggal, sedangkan bar chart digunakan untuk membandingkan penjualan antar-cabang dan melihat jumlah item terjual berdasarkan menu.

### [Embun Bigar Hidayat - Anggota 5]

Pada tugas ini saya belajar bahwa dashboard harus menyajikan informasi dengan sederhana dan mudah dipahami oleh pengguna. Penggunaan KPI membantu menampilkan informasi utama secara cepat, sedangkan grafik digunakan untuk memberikan gambaran yang lebih detail mengenai tren, cabang, dan menu.

Saya juga memahami pentingnya peer review dalam proses pembuatan prototype. Masukan dari kelompok lain dapat digunakan untuk memperbaiki tata letak, ukuran visual, kejelasan informasi, dan penggunaan filter agar dashboard lebih mudah digunakan.

## Daftar Kontribusi

| Anggota                          | Bagian yang Dikerjakan                     | Persentase Kontribusi |
| -------------------------------- | ------------------------------------------ | --------------------- |
| Isyaka Dhafa Maulana             | Aktivitas 3 — Prototype Power BI           | 20%                   |
| Habrian Daffa Dwiyandana         | Aktivitas 2 — Wireframe                    | 20%                   |
| Mohamad Safi'i                   | Aktivitas 4 — Peer Review                  | 20%                   |
| Muhammad Irfan Mukasyaf Al Fuady | Aktivitas 1 — Audience-Task-Context        | 20%                   |
| Embun Bigar Hidayat              | Aktivitas 2 — Alasan dan Penjelasan Visual | 20%                   |
| **Total**                        |                                            | **100%**              |

## Checklist

* [✓] ATC tercatat
* [✓] Wireframe + alasan visual
* [ ] Prototype screenshot (>=3 visual + slicer)
* [ ] Peer review ke kelompok lain
* [✓] Refleksi perubahan + refleksi anggota + kontribusi 100%
* [ ] >=10 commit
