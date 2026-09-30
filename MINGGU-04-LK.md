## Lembar Kerja Mahasiswa (LK) — Pertemuan 6

### Tugas 4: Dashboard Design (Wireframe & Prototype)

> **PETUNJUK:** Copy ke `kel-XX/minggu-06/LK.md`. Commit min 10x. Screenshot
> wireframe & prototype. Push sebelum akhir sesi.

### Identitas

| Field    | Isi                           |
| -------- | ----------------------------- |
| Kelas    | SI-C                          |
| Kelompok | 06                            |
| Sub-CPMK | Sub-CPMK03 — Dashboard Design |
| Bobot    | 2% (Tugas 4)                  |

### Aktivitas 1 — Audience-Task-Context (1 paragraf)

####Audience

Dashboard ditujukan kepada pemilik atau pengelola Mie Ayam Afui yang membutuhkan informasi penjualan dari tiga cabang untuk membantu melihat kondisi penjualan, menu, dan performa masing-masing cabang.

####Task

Dashboard digunakan untuk melihat total penjualan, jumlah item yang terjual, menu terlaris, tren penjualan berdasarkan tanggal, perbandingan penjualan antar-cabang, serta peringkat menu pada masing-masing cabang. Kebutuhan tersebut disesuaikan dengan business question pada tugas sebelumnya dan hasil analisis `RANK()` pada LK 5.

####Context

Dashboard dibuat menggunakan Power BI dengan sumber data dari PostgreSQL Data Warehouse yang telah dibangun pada LK 3 dan diisi melalui proses ETL pada LK 4. Data yang digunakan berasal dari `fact_penjualan`, `dim_tanggal`, `dim_cabang`, `dim_menu`, dan `dim_porsi`. Data channel penjualan langsung dan ojek online serta biaya komisi belum tersedia pada model data saat ini sehingga belum digunakan dalam dashboard.

### Aktivitas 2 — Wireframe lo-fi

> Tempel foto kertas / link Excalidraw / sketsa ASCII. Sebut alasan per visual.

#### Rancangan Dashboard

**Filter yang Digunakan :**

* Filter Tanggal
* Filter Cabang
* Filter Menu

**Rancangan Tampilan**

```text
┌─────────────────────────────────────────────────────────────────┐
│             DASHBOARD PENJUALAN MIE AYAM AFUI                  │
├──────────────────┬──────────────────┬───────────────────────────┤
│ TOTAL PENJUALAN  │ TOTAL ITEM       │ MENU TERLARIS             │
│ Rp ...           │ ... item         │ ...                       │
├──────────────────┴──────────────────┴───────────────────────────┤
│                                                                 │
│                    TREN PENJUALAN                               │
│                         Line Chart                              │
│                                                                 │
├────────────────────────────────┬────────────────────────────────┤
│ PENJUALAN PER CABANG            │ TOP MENU                       │
│                                │                                │
│ Bar Chart                      │ Bar Chart                      │
│                                │                                │
└────────────────────────────────┴────────────────────────────────┘
```

**Alasan visual:**


### Penjelasan Visual

**1. KPI Total Penjualan**

Menggunakan `SUM(total_penjualan)` dari `fact_penjualan` untuk menunjukkan nilai total penjualan.

**2. KPI Total Item**

Menggunakan `SUM(jumlah_terjual)` dari `fact_penjualan` untuk menunjukkan jumlah item yang terjual.

**3. KPI Menu Terlaris**

Menampilkan menu dengan jumlah item terjual paling tinggi. Berdasarkan data pada LK 3 dan LK 4, Mie Ayam Original memiliki jumlah item terjual paling tinggi.

**4. Line Chart Tren Penjualan**

* Sumbu X: tanggal
* Sumbu Y: total penjualan

Visual digunakan untuk melihat perubahan penjualan berdasarkan tanggal.

**5. Bar Chart Penjualan per Cabang**

* Sumbu X: nama cabang
* Sumbu Y: total penjualan

Visual digunakan untuk membandingkan performa penjualan antar tiga cabang Mie Ayam Afui.

**6. Bar Chart Top Menu**

* Sumbu X: nama menu
* Sumbu Y: jumlah item terjual

Visual ini berkaitan dengan query `RANK()` pada LK 5 untuk mengetahui peringkat menu berdasarkan jumlah item yang terjual pada setiap cabang.

### Aktivitas 3 — Prototype hi-fi Power BI

> Screenshot dashboard (min. 3 visual + 1 slicer). `.pbix` opsional commit.

**Daftar visual:**

* **KPI Card Total Penjualan** — mengetahui nilai total penjualan Mie Ayam Afui.
* **KPI Card Total Item Terjual** — mengetahui jumlah item yang berhasil terjual.
* **Line Chart Tren Penjualan** — melihat perubahan penjualan berdasarkan tanggal.
* **Bar Chart Penjualan per Cabang** — membandingkan total penjualan antar-cabang.
* **Bar Chart Top Menu** — mengetahui menu dengan jumlah item terjual paling tinggi.
* **Slicer: Tanggal** — memfilter dashboard berdasarkan periode tanggal.
* **Slicer: Cabang** — memfilter dashboard berdasarkan cabang.
* **Slicer: Menu** — memfilter dashboard berdasarkan menu.

**Screenshot Prototype:**

`[Tempel screenshot dashboard Power BI di sini]`

### Aktivitas 4 — Peer Review (feedback ke 1 kelompok lain)

* **Kelompok yang direview:** `<isi kelompok yang direview>`
* **Feedback (clarity / visual / audience-fit):** Dashboard sudah memiliki informasi utama berupa KPI dan grafik yang dapat membantu pengguna melihat kondisi penjualan. Visual yang digunakan sudah sesuai dengan kebutuhan analisis, tetapi penempatan visual dan ukuran elemen perlu dibuat konsisten agar informasi utama lebih mudah ditemukan oleh pengguna.

### Refleksi

* **Perubahan desain dari wireframe → prototype berdasarkan feedback:** Setelah mendapatkan feedback, dilakukan penyesuaian terhadap penempatan dan ukuran visual agar KPI dapat terlihat lebih jelas dan grafik lebih mudah dibandingkan. Filter juga ditempatkan pada bagian atas dashboard agar pengguna dapat menggunakannya dengan mudah untuk melihat data berdasarkan tanggal, cabang, atau menu.

#### [Isyaka Dhafa Maulana — Ketua]

Pada pertemuan ini saya mempelajari bahwa pembuatan dashboard tidak hanya membuat grafik, tetapi harus dimulai dari kebutuhan pengguna dan business question. Saya menghubungkan hasil dari LK sebelumnya, mulai dari data warehouse, ETL, sampai query `RANK()` untuk menentukan informasi yang akan ditampilkan pada dashboard Mie Ayam Afui.

Saya juga belajar memahami hubungan antara wireframe dan prototype. Wireframe digunakan untuk menentukan susunan awal dashboard, sedangkan prototype Power BI digunakan untuk melihat bagaimana rancangan tersebut diterapkan pada data sebenarnya.

#### [Habrian Daffa Dwiyandana - Anggota 2]

Pada minggu ini saya belajar bahwa dashboard harus dibuat berdasarkan kebutuhan pengguna dan bukan hanya berdasarkan banyaknya visual. Setiap grafik harus memiliki tujuan yang jelas dan dapat membantu menjawab business question yang telah ditentukan sebelumnya.

Saya juga memahami bahwa hasil query analitik pada LK 5 dapat digunakan sebagai dasar dalam menentukan visual dashboard, terutama untuk melihat peringkat menu pada masing-masing cabang.

#### [Mohamad Safi'i - Anggota 3]

Pada tugas ini saya memahami bahwa dashboard merupakan bagian lanjutan dari proses BI yang sudah dilakukan pada pertemuan sebelumnya. Data dari `fact_penjualan` dan tabel dimensi dapat digunakan untuk menampilkan informasi penjualan dalam bentuk yang lebih mudah dipahami.

Saya juga memahami bahwa dashboard harus mengikuti data yang tersedia. Analisis keuntungan berdasarkan channel langsung dan ojek online belum dapat ditampilkan karena informasi channel dan biaya komisi belum tersedia dalam model data kelompok.

#### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]

Pada pertemuan ini saya belajar membuat wireframe sebelum membuat prototype dashboard di Power BI. Dengan membuat wireframe terlebih dahulu, posisi KPI, grafik, dan filter dapat dirancang agar dashboard lebih terstruktur.

Saya juga belajar memilih visual berdasarkan jenis informasi. Line chart digunakan untuk melihat tren berdasarkan waktu, sedangkan bar chart digunakan untuk membandingkan penjualan antar-cabang dan melihat jumlah penjualan menu.

#### [Embun Bigar Hidayat - Anggota 5]

Pada tugas ini saya belajar bahwa dashboard harus dapat menyampaikan informasi secara sederhana dan mudah dipahami. Penggunaan KPI dan grafik membantu pengguna mendapatkan informasi utama tanpa harus melihat data transaksi satu per satu.

Saya juga belajar pentingnya peer review karena masukan dari kelompok lain dapat digunakan untuk memperbaiki tampilan dashboard, terutama dalam hal kejelasan visual, penempatan informasi, dan kesesuaian dengan kebutuhan pengguna.

### Daftar Kontribusi

| Anggota                          | Bagian yang Dikerjakan              | Persentase Kontribusi |
| -------------------------------- | ----------------------------------- | --------------------: |
| Isyaka Dhafa Maulana             | Aktivitas 3 — Prototype Power BI    |                   20% |
| Habrian Daffa Dwiyandana         | Aktivitas 2 — Wireframe             |                   20% |
| Mohamad Safi'i                   | Aktivitas 4 — Peer Review           |                   20% |
| Muhammad Irfan Mukasyaf Al Fuady | Aktivitas 1 — Audience-Task-Context |                   20% |
| Embun Bigar Hidayat              | Aktivitas 2 — Penjelasan Visual     |                   20% |
| **Total**                        |                                     |              **100%** |

### Checklist

* [✓] ATC tercatat
* [✓] Wireframe + alasan visual
* [ ] Prototype screenshot (>=3 visual + slicer)
* [ ] Peer review ke kelompok lain
* [✓] Refleksi perubahan + refleksi anggota + kontribusi 100%
* [ ] >=10 commit
