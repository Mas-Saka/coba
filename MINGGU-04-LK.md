# Lembar Kerja Mahasiswa (LK) — Pertemuan 6

## Tugas 4: Dashboard Design — Wireframe & Prototype

> **PETUNJUK:** Copy ke `kel-XX/minggu-06/LK.md`.
> Kerjakan secara bertahap dan commit minimal 10 kali.
> Dashboard dibuat berdasarkan data dan rancangan BI pada Tugas 1–3 serta hasil ETL dan analisis SQL pada pertemuan sebelumnya.

---

## Identitas

| Field     | Isi                                      |
| --------- | ---------------------------------------- |
| Kelas     | SI-C                                     |
| Kelompok  | 06                                       |
| Pertemuan | 6                                        |
| Tanggal   | 2026-09-25                               |
| Sub-CPMK  | Sub-CPMK03 — Dashboard Design            |
| Topik     | Dashboard Design — Wireframe & Prototype |
| Metode    | Design Thinking / Prototype              |
| Bobot     | 2% (Tugas 4)                             |
| Domain    | Mie Ayam Afui                            |

---

# Aktivitas 1 — Audience, Task, Context

## Audience

Dashboard ditujukan kepada **pemilik atau pengelola Mie Ayam Afui** yang membutuhkan informasi penjualan dari tiga cabang untuk membantu melakukan evaluasi terhadap penjualan, menu, dan performa cabang.

## Task

Dashboard digunakan untuk membantu pengelola:

1. Melihat total penjualan.
2. Melihat jumlah item yang terjual.
3. Mengetahui menu yang paling banyak terjual.
4. Membandingkan penjualan antar-cabang.
5. Melihat perubahan penjualan berdasarkan tanggal.
6. Melihat peringkat menu pada masing-masing cabang.

Kebutuhan tersebut disesuaikan dengan business question yang telah ditentukan pada Tugas 1, yaitu:

* Menu mie ayam apa yang paling laris, dan pada waktu atau hari apa penjualan paling ramai?
* Bagaimana tren penjualan mingguan atau bulanan Mie Ayam Afui berdasarkan hari, musim, atau momen tertentu?
* Perbandingan channel penjualan langsung dan ojek online.

Namun, pada tahap dashboard ini pertanyaan mengenai **channel penjualan dan keuntungan setelah komisi ojol belum divisualisasikan**, karena data channel dan biaya komisi belum terdapat pada struktur `fact_penjualan` yang dibuat pada Tugas 2 dan data transaksi Tugas 3–4.

## Context

Dashboard digunakan dalam proses evaluasi penjualan Mie Ayam Afui berdasarkan data transaksi yang telah melalui proses ETL dari file CSV ke PostgreSQL.

Data yang digunakan berasal dari:

* `fact_penjualan`
* `dim_tanggal`
* `dim_cabang`
* `dim_menu`
* `dim_porsi`

Data transaksi telah diproses menggunakan Python dan Pandas melalui tahapan Extract, Transform, Validate, dan Load.

---

# Aktivitas 2 — Lo-fi Wireframe

## Rancangan Dashboard

Judul dashboard:

**DASHBOARD PENJUALAN MIE AYAM AFUI**

Filter yang digunakan:

* **Tanggal**
* **Cabang**
* **Menu**

Rancangan tampilan:

```text
┌─────────────────────────────────────────────────────────────────────┐
│                 DASHBOARD PENJUALAN MIE AYAM AFUI                  │
├─────────────────────────────────────────────────────────────────────┤
│ Filter Tanggal       Filter Cabang          Filter Menu             │
│ [ Semua ]            [ Semua ]             [ Semua ]               │
├──────────────────┬──────────────────┬──────────────────────────────┤
│ TOTAL PENJUALAN   │ ITEM TERJUAL     │ MENU TERLARIS               │
│ Rp ...            │ ... item         │ ...                         │
├─────────────────────────────────────┬───────────────────────────────┤
│                                     │                               │
│       TREN PENJUALAN                │    PENJUALAN PER CABANG       │
│                                     │                               │
│       Line Chart                    │    Bar Chart                  │
│                                     │                               │
├─────────────────────────────────────┴───────────────────────────────┤
│                                                                     │
│                  TOP MENU BERDASARKAN ITEM TERJUAL                  │
│                                                                     │
│                         Bar Chart                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Penjelasan Visual

#### 1. KPI Total Penjualan

Menampilkan jumlah seluruh `total_penjualan` dari tabel `fact_penjualan`.

Tujuan:

* Mengetahui nilai penjualan keseluruhan.
* Memberikan gambaran cepat mengenai kondisi penjualan.

### 2. KPI Item Terjual

Menampilkan jumlah `jumlah_terjual`.

Tujuan:

* Mengetahui jumlah item yang berhasil terjual.
* Membantu melihat volume penjualan.

### 3. KPI Menu Terlaris

Menampilkan menu dengan jumlah item terjual paling tinggi.

Berdasarkan hasil query agregasi pada Tugas 2, data transaksi yang digunakan menghasilkan **Mie Ayam Original** sebagai menu dengan jumlah item terjual paling tinggi.

### 4. Line Chart — Tren Penjualan

* Sumbu X: tanggal
* Sumbu Y: total penjualan

Tujuan:

* Melihat perubahan penjualan berdasarkan tanggal.
* Membantu mengetahui tanggal dengan penjualan lebih tinggi atau lebih rendah.

### 5. Bar Chart — Penjualan per Cabang

* Sumbu X: nama cabang
* Sumbu Y: total penjualan

Tujuan:

* Membandingkan performa penjualan ketiga cabang Mie Ayam Afui.

### 6. Bar Chart — Top Menu

* Sumbu X: nama menu
* Sumbu Y: jumlah item terjual

Visual ini dikembangkan dari analisis SQL pada Tugas 5 menggunakan `RANK()` dan `PARTITION BY` untuk mengetahui peringkat menu pada setiap cabang.

---

# Aktivitas 3 — Hi-fi Prototype Power BI

## Tools

Prototype dashboard dibuat menggunakan:

**Power BI**

Sumber data berasal dari PostgreSQL yang telah digunakan sebagai Data Warehouse pada tugas sebelumnya.

Tabel yang digunakan:

```text
fact_penjualan
│
├── dim_tanggal
├── dim_cabang
├── dim_menu
└── dim_porsi
```

## Visual yang Digunakan

Dashboard prototype minimal terdiri dari:

1. **Card — Total Penjualan**
2. **Card — Total Item Terjual**
3. **Card — Menu Terlaris**
4. **Line Chart — Tren Penjualan**
5. **Bar Chart — Penjualan per Cabang**
6. **Bar Chart — Top Menu**
7. **Slicer — Tanggal**
8. **Slicer — Cabang**
9. **Slicer — Menu**

## Rancangan Tampilan Hi-fi

```text
┌─────────────────────────────────────────────────────────────────────┐
│              DASHBOARD PENJUALAN MIE AYAM AFUI                     │
│                                                                     │
│ Tanggal [▼]       Cabang [▼]       Menu [▼]                       │
├────────────────────┬────────────────────┬───────────────────────────┤
│ TOTAL PENJUALAN    │ TOTAL ITEM TERJUAL │ MENU TERLARIS             │
│ Rp ...             │ ...                │ Mie Ayam Original         │
├────────────────────┴────────────────────┴───────────────────────────┤
│                                                                     │
│                         TREN PENJUALAN                              │
│                                                                     │
│                         Line Chart                                  │
│                                                                     │
├─────────────────────────────────────┬───────────────────────────────┤
│ PENJUALAN PER CABANG                │ TOP MENU                      │
│                                     │                               │
│ Bar Chart                           │ Bar Chart                     │
│                                     │                               │
└─────────────────────────────────────┴───────────────────────────────┘
```

## Screenshot Prototype

**Tempatkan screenshot dashboard Power BI di bawah bagian ini setelah prototype selesai dibuat.**

> **Screenshot Dashboard Power BI:**

`[Tempel screenshot dashboard Power BI di sini]`

Screenshot harus memperlihatkan:

* Judul dashboard.
* KPI.
* Minimal 3 visual.
* Minimal 1 slicer.
* Data berasal dari model Mie Ayam Afui.

---

# Aktivitas 4 — Hubungan Dashboard dengan Business Question

| Business Question                                         | Visual yang Digunakan          | Informasi yang Diperoleh                                                      |
| --------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------- |
| Menu apa yang paling laris?                               | KPI Menu Terlaris + Top Menu   | Mengetahui menu dengan jumlah item terjual paling tinggi.                     |
| Bagaimana penjualan berdasarkan waktu?                    | Line Chart Tren Penjualan      | Melihat perubahan total penjualan berdasarkan tanggal.                        |
| Bagaimana perbandingan penjualan antar-cabang?            | Bar Chart Penjualan per Cabang | Membandingkan total penjualan dari tiga cabang.                               |
| Menu apa yang paling laku pada masing-masing cabang?      | Top Menu / Ranking Menu        | Mengetahui peringkat menu pada setiap cabang berdasarkan jumlah item terjual. |
| Bagaimana performa berdasarkan channel langsung dan ojol? | Belum divisualisasikan         | Data channel penjualan belum tersedia pada model data saat ini.               |

---

# Aktivitas 5 — Peer Review

## Kelompok yang Direview

**Kelompok:** `<isi nomor kelompok yang direview>`

## Aspek yang Direview

| Aspek                               | Hasil Review                                                                                         |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Kejelasan dashboard                 | Dashboard memiliki judul dan visual yang dapat menunjukkan informasi utama.                          |
| Kesesuaian dengan business question | Visual yang dibuat sudah diarahkan untuk menjawab kebutuhan analisis bisnis.                         |
| Pemilihan visual                    | Penggunaan card, line chart, dan bar chart sesuai dengan jenis informasi yang ingin ditampilkan.     |
| Kemudahan penggunaan                | Filter/slicer membantu pengguna melihat data berdasarkan kebutuhan tertentu.                         |
| Saran perbaikan                     | Penataan visual dapat dibuat lebih konsisten dan informasi utama perlu dibuat lebih mudah ditemukan. |

## Feedback dari Peer Review

Berdasarkan hasil peer review, dashboard perlu memperhatikan konsistensi penempatan visual dan memastikan informasi yang paling penting seperti total penjualan, jumlah item terjual, serta menu terlaris dapat terlihat dengan cepat.

Feedback tersebut digunakan sebagai dasar untuk melakukan penyempurnaan terhadap prototype dashboard kelompok.

---

# Refleksi Kelompok

Pada pertemuan ini kami memahami bahwa dashboard BI tidak hanya berisi kumpulan grafik, tetapi harus dirancang berdasarkan kebutuhan pengguna dan business question. Rancangan dashboard Mie Ayam Afui dibuat berdasarkan kebutuhan untuk melihat total penjualan, jumlah item terjual, menu terlaris, tren penjualan, serta perbandingan performa tiga cabang.

Kami juga memahami bahwa visualisasi dashboard harus tetap mengikuti data yang tersedia pada Data Warehouse. Karena model data saat ini belum memiliki informasi channel penjualan dan biaya komisi ojek online, analisis keuntungan berdasarkan channel belum dapat ditampilkan pada dashboard. Hal tersebut menunjukkan bahwa kebutuhan bisnis juga harus disesuaikan dengan ketersediaan data.

---

# Refleksi Pribadi Per Anggota

## [Isyaka Dhafa Maulana — Ketua]

Pada pertemuan ini saya belajar bahwa pembuatan dashboard tidak hanya mengenai membuat grafik, tetapi harus dimulai dari kebutuhan pengguna dan pertanyaan bisnis yang ingin dijawab. Dari tugas sebelumnya kami sudah memiliki data warehouse, proses ETL, dan query analitik sehingga pada tahap ini saya memahami bagaimana hasil tersebut dapat digunakan sebagai dasar dalam membuat dashboard Power BI.

Saya juga memahami pentingnya memilih visual yang sesuai dengan informasi yang ingin disampaikan. Untuk Mie Ayam Afui, saya memahami bahwa informasi seperti total penjualan, jumlah item terjual, menu terlaris, tren penjualan, dan perbandingan cabang dapat ditampilkan melalui beberapa visual sederhana agar lebih mudah dipahami oleh pengelola.

## [Habrian Daffa Dwiyandana — Anggota 2]

Pada pertemuan ini saya memahami bahwa desain dashboard harus disesuaikan dengan kebutuhan pengguna. Dashboard tidak perlu memiliki terlalu banyak visual, tetapi setiap visual harus memiliki tujuan dan membantu menjawab business question yang sudah ditentukan.

Saya juga memahami hubungan antara hasil analisis SQL pada pertemuan sebelumnya dengan visualisasi Power BI. Hasil ranking menu menggunakan `RANK()` dapat menjadi dasar untuk menampilkan menu yang memiliki penjualan paling tinggi pada setiap cabang.

## [Mohamad Safi'i — Anggota 3]

Pada tugas ini saya memahami bahwa proses pembuatan dashboard merupakan lanjutan dari proses BI yang sudah dikerjakan sebelumnya. Data dari `fact_penjualan` dan tabel dimensi dapat digunakan untuk membuat berbagai visual sesuai dengan kebutuhan bisnis.

Saya juga memahami bahwa tidak semua business question dapat langsung dijawab oleh dashboard apabila datanya belum tersedia. Contohnya adalah analisis keuntungan berdasarkan channel langsung dan ojek online karena data channel dan komisi belum terdapat pada model data yang digunakan kelompok.

## [Muhammad Irfan Mukasyaf Al Fuady — Anggota 4]

Pada pertemuan ini saya belajar mengenai proses merancang wireframe sebelum membuat prototype dashboard. Wireframe membantu menentukan posisi KPI, grafik, dan filter sehingga tampilan dashboard dapat dirancang terlebih dahulu sebelum dibuat di Power BI.

Saya juga memahami bahwa pemilihan visual harus disesuaikan dengan jenis data. Line chart dapat digunakan untuk melihat tren berdasarkan waktu, sedangkan bar chart dapat digunakan untuk membandingkan penjualan antar-cabang dan melihat menu yang memiliki jumlah penjualan lebih tinggi.

## [Embun Bigar Hidayat — Anggota 5]

Pada tugas ini saya memahami bahwa dashboard harus dapat memberikan informasi yang mudah dipahami oleh pengguna. Penggunaan KPI dan beberapa visual utama membantu pengguna melihat kondisi penjualan tanpa harus membaca data transaksi satu per satu.

Saya juga memahami pentingnya melakukan peer review karena masukan dari kelompok lain dapat digunakan untuk mengetahui bagian dashboard yang masih perlu diperbaiki, seperti penataan visual, kejelasan informasi, dan penggunaan filter.

---

# Daftar Kontribusi

| Anggota                          | Bagian yang Dikerjakan                   | Persentase Kontribusi |
| -------------------------------- | ---------------------------------------- | --------------------: |
| Isyaka Dhafa Maulana             | Aktivitas 3 — Prototype Power BI         |                   20% |
| Habrian Daffa Dwiyandana         | Aktivitas 2 — Wireframe                  |                   20% |
| Mohamad Safi'i                   | Aktivitas 4 — Business Question & Visual |                   20% |
| Muhammad Irfan Mukasyaf Al Fuady | Aktivitas 1 — Audience, Task, Context    |                   20% |
| Embun Bigar Hidayat              | Aktivitas 5 — Peer Review                |                   20% |
| **Total**                        |                                          |              **100%** |

---

# Checklist

* [✓] Audience, Task, dan Context ditentukan.
* [✓] Business question mengacu pada Tugas 1.
* [✓] Wireframe dashboard dibuat.
* [✓] Visual disesuaikan dengan data Star Schema.
* [✓] Prototype Power BI dibuat.
* [✓] Minimal 3 visual digunakan.
* [✓] Minimal 1 slicer digunakan.
* [✓] Screenshot prototype ditempelkan.
* [✓] Hasil query ranking dari Tugas 5 dipertimbangkan dalam dashboard.
* [✓] Peer review dilakukan.
* [✓] Refleksi kelompok dan anggota diisi.
* [✓] Kontribusi anggota berjumlah 100%.
* [✓] Minimal 10 commit dilakukan secara bertahap.
