# Lembar Kerja Mahasiswa (LK) — Pertemuan 5 (FORMATIF, bobot 0%)
## Advanced SQL untuk BI — Presentasi & Information-gap

> **FORMATIF** — tidak masuk nilai sumatif. Kerjakan untuk penguatan skill sebelum
> blok visualisasi (minggu 6-7). Copy ke `kel-XX/minggu-05/LK.md`. Tetap commit bertahap.

## Identitas
| Field | Isi |
|---|---|
| Kelas | SI-C |
| Kelompok | 06 |
| Tanggal | 2026-09-22 |
| Sub-CPMK | Sub-CPMK02 — Advanced SQL (formatif) |
| Bobot | 0% (feedback saja) |

## Aktivitas 1 — Query Analitik Kelompok (window/CTE)
> Tempel 1 query window function atau CUE dari kelompok + jelaskan maksud bisnisnya.

```sql
SELECT
    c.cabang_name,
    m.menu_name,
    SUM(f.jumlah_terjual) AS total_item_terjual,
    RANK() OVER (
        PARTITION BY c.cabang_id
        ORDER BY SUM(f.jumlah_terjual) DESC
    ) AS peringkat_menu
FROM fact_penjualan f
JOIN dim_cabang c
    ON f.cabang_id = c.cabang_id
JOIN dim_menu m
    ON f.menu_id = m.menu_id
GROUP BY
    c.cabang_id,
    c.cabang_name,
    m.menu_id,
    m.menu_name
ORDER BY
    c.cabang_name,
    peringkat_menu;
```

**Maksud bisnis:** 
<Query ini dipakai untuk mengetahui menu apa yang paling laku di setiap cabang Mie Ayam Afui. Total item terjual dihitung per menu, lalu diberi peringkat dengan RANK() yang dipisah per cabang (PARTITION BY cabang_id), jadi peringkat 1 di tiap cabang adalah menu terlaris di cabang itu. Hasilnya membantu pemilik dalam menentukan menu andalan tiap cabang, menyiapkan stok bahan baku sesuai menu yang paling banyak dicari, serta menemukan menu yang peringkatnya rendah di suatu cabang untuk dievaluasi, misalnya dipromosikan atau dikurangi porsi stoknya. Karena pakai window function, data tiap menu tetap tampil lengkap dan tidak hilang seperti kalau hanya memakai GROUP BY>

## Aktivitas 2 — EXPLAIN ANALYZE
> Query yang digunakan:
EXPLAIN ANALYZE
SELECT
    m.menu_name,
    SUM(f.jumlah_terjual) AS total_item_terjual
FROM fact_penjualan f
JOIN dim_menu m
    ON f.menu_id = m.menu_id
WHERE f.tanggal_id BETWEEN 1 AND 6
GROUP BY m.menu_name
ORDER BY total_item_terjual DESC;
- Jenis scan: Pada dataset Mie Ayam Afui yang masih berjumlah relatif sedikit, PostgreSQL dapat menggunakan Seq Scan pada tabel fact_penjualan. Hal ini terjadi karena jumlah data masih kecil sehingga membaca seluruh baris dapat dianggap lebih efisien daripada menggunakan index.
- Analisis: Untuk kondisi data saat ini, penambahan index khusus pada tanggal_id belum tentu memberikan peningkatan performa yang terlihat karena jumlah data masih sedikit. Pada LK-03 kelompok sudah membuat index pada tanggal_id, cabang_id, menu_id, dan porsi_id untuk mendukung kebutuhan query analitik dan JOIN.

## Aktivitas 3 — Information-gap (refleksi)
- Query yang paling sulit disatukan saat pairing: <Query yang paling sulit disatukan adalah query ranking menu per cabang karena perlu menggabungkan beberapa bagian, yaitu JOIN antara tabel fakta dan dimensi, GROUP BY untuk menghitung jumlah penjualan, serta RANK() OVER (PARTITION BY ...) untuk membuat peringkat pada setiap cabang. Setiap bagian query harus ditempatkan dengan benar agar hasil ranking sesuai dengan kebutuhan analisis.>
- Pelajaran yang didapat: <Dari kegiatan information-gap, kami belajar bahwa membuat query SQL. lanjut tidak hanya membutuhkan pemahaman sintaks, tetapi juga komunikasi antaranggota. Setiap bagian query yang dimiliki harus dipahami terlebih dahulu sebelum digabungkan menajdi query utuh. Kami juga menjadi lebih memahami penggunaan window function, khususnya RANK() dan PARTITION BY, untuk kebutuhan analisis BI.>

## Refleksi Pribadi Per Anggota
> Wajib masing-masing anggota (1-2 paragraf). 

### [Isyaka Dhafa Maulana — Ketua]
<Pada pertemuan ini saya mempelajari penggunaan window function, khususnya RANK() dan PARTITION BY, untuk membuat peringkat menu berdasarkan jumlah item yang terjual pada setiap cabang. Awalnya saya masih agak bingung membedakan penggunaan PARTITION BY dengan GROUP BY, tetapi setelah mencoba query dan melihat hasilnya saya mulai memahami bahwa PARTITION BY digunakan untuk membagi data menjadi beberapa kelompok tanpa menghilangkan hasil data yang dibutuhkan.

Selain itu, saya ikut memahami hasil EXPLAIN ANALYZE pada query yang digunakan. Dari hasil tersebut, query menggunakan Seq Scan pada dim_menu dan fact_penjualan, kemudian menggunakan Hash Join dan HashAggregate. Saya belajar bahwa penggunaan Seq Scan masih sesuai karena jumlah data yang digunakan masih sedikit. Dari kegiatan ini saya mendapatkan pengalaman dalam menyusun query analitik dan membaca execution plan PostgreSQL>

### [Habrian Daffa Dwiyandana - Anggota 2]
<Pada minggu ke-5 ini saya belajar lebih memahami penggunaan window function dalam SQL, terutama RANK() dan PARTITION BY. Saya memahami bahwa window function dapat digunakan untuk memberikan peringkat tanpa menghilangkan baris hasil query seperti yang terjadi pada proses agregasi biasa.

Saya juga belajar bahwa query analitik harus disesuaikan dengan pertanyaan bisnis. Dalam kasus Mie Ayam Afui, ranking menu dapat digunakan untuk mengetahui menu yang paling banyak terjual pada setiap cabang. Dari kegiatan information-gap, saya juga belajar bahwa setiap query perlu dikomunikasikan dengan jelas agar dapat digabungkan menjadi query yang benar.>

### [Mohamad Safi'i - Anggota 3]
<Minggu ini saya kebagian maksud bisnis buat query ranking menu per cabang, dan ternyata lumayan bikin mikir juga, karena bukan cuma soal query jalan, tapi juga harus bisa jelasin buat apa dipakai. Dari situ jadi paham kalau RANK() sama PARTITION BY itu berguna buat ngeliat menu apa yang paling laku di tiap cabang, jadi pemilik bisa nyiapin stok sesuai menu yang paling dicari. Saya ngerti bedanya sama GROUP BY: kalau GROUP BY barisnya digabung, sedangkan window function barisnya tetap utuh dan cuma nambah kolom peringkat. Terus soal EXPLAIN ANALYZE, ternyata Seq Scan itu gak selalu jelek.>

### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]
<Pada tugas minggu ke-5 ini saya belajar tentang penggunaan query SQL yang lebih lanjut untuk melakukan analisis data. Saya mulai memahami bahwa GROUP BY dan window function memiliki fungsi yang berbeda. GROUP BY digunakan untuk menggabungkan data menjadi hasil agregasi, sedangkan window function tetap mempertahankan baris dan menambahkan hasil perhitungan pada setiap baris.

Selain itu, saya belajar mengenai EXPLAIN ANALYZE untuk melihat rencana dan waktu eksekusi query. Dari kegiatan ini saya menjadi lebih memahami bahwa optimasi query tidak hanya dilakukan dengan mengubah query, tetapi juga perlu melihat bagaimana database menjalankan query tersebut.>

### [Embun Bigar Hidayat - Anggota 5]
<Pada tugas ini saya belajar bahwa membuat query SQL membutuhkan ketelitian, terutama saat menggabungkan `JOIN`, `GROUP BY`, dan `RANK()`. Dari kegiatan pairing, saya belajar pentingnya berdiskusi dengan anggota kelompok agar setiap bagian query dapat disatukan dengan benar. Saya juga menjadi lebih paham bahwa `RANK()` dapat digunakan untuk mengetahui peringkat menu berdasarkan jumlah penjualan pada setiap cabang.
>

## Checklist
- [✓] 1 query window/CTE + maksud bisnis
- [✓] EXPLAIN ringkas + analisis
- [✓] Refleksi information-gap
- [✓] Refleksi anggota
