# Lembar Kerja Mahasiswa (LK) — Pertemuan 3
## Tugas 2: Data Model Design (Dimensional Modeling di PostgreSQL)

> **PETUNJUK PENGISIAN (wajib dibaca dulu):**
>
> 1. **Copy** file ini ke folder kelompok Anda: `kel-XX/minggu-03/LK.md`.
> 2. **Ganti** semua placeholder `<...>` dengan konten Anda.
> 3. **Commit bertahap** — minimal 10 commit. Sertakan file `.sql` DDL.
> 4. **Push** sebelum akhir sesi kelas.
> 5. **Jangan** hapus/ubah git history.
> 6. **Jangan** edit folder kelompok lain.

---

## Identitas

| Field | Isi |
|---|---|
| Kelas | SI-C (pilih sesuai repo Anda) |
| Kelompok | 06 |
| Pertemuan | 3 |
| Tanggal | 2026-09-09 |
| Sub-CPMK | Sub-CPMK02 — Data warehouse & dimensional modeling |
| Topik | Data Model Design |
| Metode | Lab session hands-on (PostgreSQL) |
| Bobot | 3% (Tugas 2) |
| Domain | (sama dengan Tugas 1 minggu 2) |

---

## Aktivitas 1 — Kimball Four-Step Process

| Langkah | Hasil untuk domain Anda |
|---|---|
| 1. Business process | Proses penjualan makanan dan minuman pada tiga cabang Mie Ayam Afui. |
| 2. Grain | Satu baris pada fact table merepresentasikan satu menu yang terjual dalam satu transaksi pada satu waktu dan satu cabang. |
| 3. Dimensions | Dimensi Tanggal/Waktu, Cabang, Menu, dan Porsi. |
| 4. Facts (measures) | Jumlah item terjual (additive), Total penjualan (additive),  Diskon (additive), Harga satuan (non-additive). |

### Catatan Commit Aktivitas Ini
- commit 1: `Menambahkan Kimball Four-Step Process untuk Mie Ayam Afui`

---

## Aktivitas 2 — Pilihan Skema & SCD

**Skema dipilih:** Star *

**Justifikasi:**
<Skema Star Schema dipilih karena sangat relevan dengan framework Kimball dan karakteristik proses bisnis UMKM Mie Ayam Afui yang difokuskan pada analisis penjualan. Pada skema ini, fact table (fact_penjualan) berada di pusat dan berelasi langsung dengan tabel-tabel dimensi secara radial. Struktur ini memberikan performa query yang optimal karena pembacaan data hanya membutuhkan satu tingkat JOIN, sehingga mempercepat proses penarikan data saat pembuatan dashboard.  

Untuk Mie Ayam Afui, fact table fact_penjualan akan terhubung langsung dengan: 
- dim_date
- dim_cabang
- dim_menu
- dim_porsi

dengan struktur ini, pengelola Mie ayam Afui dapat melakukan analisis seperti mencari menu paling laris, menghitung total penjualan per cabang, penjualan berdasarkan porsi, tren penjualan dan perbandingan performa tiga cabang.  Skema juga tetap dapat dikembangkan apabila Mie Ayam Afui menambah cabang atau kebutuhan analisis lainnya.>

**SCD (di dimensi mana & tipe apa):**
- Dim menu → SCD Type 2 — alasan: digunakan apabila atribut menu seperti kategori atau harga mengalami perubahan dan perubahan tersebut perlu tetap dapat dilacak secara historis. CD Type 2 membuat baris baru untuk versi dimensi yang baru sehingga transaksi lama tetap mengacu pada versi menu yang berlaku pada saat transaksi terjadi. Materi menjelaskan bahwa SCD Type 2 membutuhkan surrogate key dan atribut seperti effective date serta status current. 
- Dim cabang → SCD Type 1 — alasan: perubahan informasi cabang seperti koreksi nama atau informasi wilayah tidak harus mempertahankan histori dalam konteks analisis penjualan ini, sehingga nilai dapat diperbarui langsung.
- Dim Tanggal → tidak menggunakan SCD — alasan: atribut tanggal bersifat tetap dan digunakan sebagai dimensi waktu untuk analisis.
- Dim Porsi → SCD Type 1 — alasan: Perubahan informasi deskriptif prosi tidak menjadi fokus histori pada analisis penjualan. 


### Catatan Commit
- commit 1 : Menentukan pilihan skema, menjelaskan justifikasi, dan menambahkan keputusan SCD

---

## Aktivitas 3 — Diagram Skema
```
<                 
                    ┌─────────────────────┐
                    │    DIM_TANGGAL      │
                    ├─────────────────────┤
                    │ PK tanggal_key      │
                    │ tanggal             │
                    │ hari                │
                    │ bulan               │
                    │ tahun               │
                    └──────────┬──────────┘
                               │
                               │
┌─────────────────────┐        │        ┌─────────────────────┐
│      DIM_MENU       │        │        │     DIM_CABANG      │
├─────────────────────┤        │        ├─────────────────────┤
│ PK menu_key         │        │        │ PK cabang_key       │
│ nama_menu           │        │        │ nama_cabang         │
│ kategori            │        │        │ lokasi              │
│ harga               │        │        └──────────┬──────────┘
└──────────┬──────────┘        │                   │
           │                   │                   │
           │                   │                   │
           └───────────────────┼───────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FACT_PENJUALAN    │
                    ├─────────────────────┤
                    │ PK penjualan_key    │
                    │ FK tanggal_key      │
                    │ FK menu_key         │
                    │ FK cabang_key       │
                    │ jumlah_terjual      │
                    │ total_penjualan     │
                    │ harga_satuan        │
                    └─────────────────────┘
>
                    
```

```

## Aktivitas 4 — DDL PostgreSQL

> *Tempel CREATE TABLE lengkap (fact + min 3 dimensi) dengan PK/FK/CHECK +
> min 2 index. Boleh juga commit file `.sql` terpisah di folder ini.*
> *Pastikan DDL ini sudah dijalankan & berhasil di PostgreSQL Anda.*

```sql
-- ============ DIMENSIONS ============
CREATE TABLE dim_date (
    -- ...
);
CREATE TABLE dim_outlet (
    -- ...
);
CREATE TABLE dim_menu (
    -- ... (dengan kolom SCD Type 2 bila dipilih)
);

-- ============ FACT ============
CREATE TABLE fact_sales (
    -- ... PK, FK, CHECK
);

-- ============ INDEXES (min 2) ============
CREATE INDEX ... ON fact_sales(...);
CREATE INDEX ... ON fact_sales(...);
```

---

## Aktivitas 5 — Seed Data & Verifikasi Query

**Seed data (min 10 baris fact):**
```sql
INSERT INTO fact_sales (...) VALUES
    (...), (...), ... ;   -- min 10 baris
```

**Query agregasi contoh (yang berhasil dijalankan):**
```sql
-- Contoh: penjualan per menu per bulan
SELECT m.menu_name, d.month_name, SUM(f.amount)
FROM fact_sales f
JOIN dim_menu m ON f.menu_id = m.menu_id
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY m.menu_name, d.month_name;
```

**Hasil (screenshot/teks):**
<tempel hasil query atau screenshot link>

### Catatan Commit
- ...

---

## Aktivitas 6 — Keputusan Desain (min 2)

| Keputusan | Pilihan | Alasan |
|---|---|---|
| <mis. amount: generated vs ETL?> | <pilihan> | <alasan> |
| <mis. SK vs natural key?> | <pilihan> | <alasan> |

---

## Refleksi Pribadi Per Anggota

> **Wajib diisi masing-masing anggota.** Pribadi & reflektif. 

### [Isyaka Dhafa Maulana — Ketua]
<refleksi>

### [Habrian Daffa Dwiyandana - Anggota 2]
<Pada pertemuan ini saya mempelajari bagaimana framework Kimball yang dipilih pada minggu sebelumnya diterapkan lebih lanjut dalam bentuk dimensional modeling. Saya memahami bahwa Star Schema memiliki fact table sebagai pusat dan dimensi yang langsung terhubung sehingga struktur data lebih sederhana untuk digunakan dalam analisis.

Saya juga memahami penggunaan SCD Type 2 pada dimensi menu. Perubahan informasi seperti harga menu tidak selalu berarti data lama harus diubah, karena histori perubahan dapat dibutuhkan untuk analisis. Dengan SCD Type 2, versi lama dan versi baru dapat disimpan sehingga transaksi dapat tetap merepresentasikan kondisi menu pada saat transaksi terjadi.>

### [Mohamad Safi'i - Anggota 3]
<refleksi>

### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]
<Dari aktivitas ini saya memahami bahwa star schema digunakan untuk menyusun data agar lebih mudah dianalisis. Tabel fakta menjadi pusat penyimpanan data yang berkaitan dengan transaksi, sedangkan tabel dimensi memberikan konteks seperti waktu, menu, dan cabang. Dengan struktur tersebut, proses analisis dan pembuatan dashboard BI dapat dilakukan dengan lebih terarah.

Saya juga memahami bahwa perancangan skema harus disesuaikan dengan kebutuhan bisnis, bukan hanya berdasarkan struktur database. Melalui pembuatan diagram skema, saya menjadi lebih memahami hubungan antara tabel fakta dan tabel dimensi serta bagaimana data dapat dipersiapkan untuk mendukung pengambilan keputusan.

### [Embun Bigar Hidayat - Anggota 5]
<Pada tugas ini, saya memahami bahwa data warehouse perlu dirancang berdasarkan proses bisnis, grain, dimensi, dan fakta. Saya juga belajar membedakan dimensi sebagai sudut pandang analisis dan measures sebagai nilai yang diukur. Aktivitas ini membantu saya memahami bagaimana kebutuhan bisnis diubah menjadi struktur data untuk analisis penjualan.>

---

## Daftar Kontribusi

| Anggota | Bagian yang Dikerjakan | Persentase Kontribusi |
|---|---|---|
| Isyaka Dhafa Maulana |  | % |
| Habrian Daffa Dwiyandana |  | % |
| Mohamad Safi'i |  | % |
| Muhammad Irfan Mukasyaf Al Fuady |  | % |
| Embun Bigar Hidayat |  | % |
| **Total** | | **100%** |

---

## Checklist Sebelum Push Final

- [ ] Four-step terisi (grain atomik)
- [ ] Pilihan star/snowflake + SCD + justifikasi
- [ ] Diagram skema
- [ ] DDL lengkap & **berhasil dijalankan** (PK/FK/CHECK + min 2 index)
- [ ] Seed data min 10 baris fact + 1 query agregasi sukses
- [ ] Min 2 keputusan desain + alasan
- [ ] Refleksi pribadi semua anggota
- [ ] Daftar kontribusi total 100%
- [ ] Min 10 commit deskriptif + push sebelum deadline

---

## Contoh Workflow Commit

```bash
mkdir -p kel-01/minggu-03 && cp MINGGU-03-LK.md kel-01/minggu-03/LK.md
# aktivitas 1 (four-step)
git add kel-01/minggu-03/ && git commit -m "Four-step: grain item-level, dim date/outlet/menu" && git push
# aktivitas 4 (DDL) — commit .sql terpisah juga OK
git add kel-01/minggu-03/LK.md kel-01/minggu-03/schema.sql && git commit -m "DDL: fact_sales + 3 dim dengan PK/FK/CHECK & index" && git push
# aktivitas 5 (seed + query)
git add kel-01/minggu-03/ && git commit -m "Seed 10 baris fact + query agregasi sukses" && git push
```
