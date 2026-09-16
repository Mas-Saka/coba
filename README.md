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
- dim_menu<img width="712" height="332" alt="image" src="https://github.com/user-attachments/assets/052d934e-4a10-4beb-9e70-2c16965cf6a8" />

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
                
                    ┌─────────────────────┐
                    │     DIM_TANGGAL     │
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
│ effective_date      │        │                   │
│ end_date            │        │                   │
│ is_current          │        │                   │
└──────────┬──────────┘        │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           │                   │                   │
           └───────────────────┼───────────────────┘
                               │
                               │
                    ┌──────────┴──────────┐
                    │   FACT_PENJUALAN    │
                    ├─────────────────────┤
                    │ PK penjualan_key    │
                    │ FK tanggal_key      │
                    │ FK menu_key         │
                    │ FK cabang_key       │
                    │ FK porsi_key        │
                    │ jumlah_terjual      │
                    │ total_penjualan     │
                    │ diskon              │
                    │ harga_satuan        │
                    └──────────┬──────────┘
                               │
                               │
                    ┌──────────▼──────────┐
                    │      DIM_PORSI      │
                    ├─────────────────────┤
                    │ PK porsi_key        │
                    │ nama_porsi          │
                    │ keterangan          │
                    └─────────────────────┘

    


```
## Aktivitas 4 — DDL PostgreSQL

> *Tempel CREATE TABLE lengkap (fact + min 3 dimensi) dengan PK/FK/CHECK +
> min 2 index. Boleh juga commit file `.sql` terpisah di folder ini.*
> *Pastikan DDL ini sudah dijalankan & berhasil di PostgreSQL Anda.*

```sql
-- ============ DIMENSIONS ============
CREATE TABLE dim_tanggal (
    tanggal_id SERIAL PRIMARY KEY,
    tanggal_actual DATE NOT NULL UNIQUE,
    hari_ke SMALLINT NOT NULL
        CHECK (hari_ke BETWEEN 1 AND 7),
    nama_hari VARCHAR(15) NOT NULL,
    bulan_ke SMALLINT NOT NULL
        CHECK (bulan_ke BETWEEN 1 AND 12),
    nama_bulan VARCHAR(15) NOT NULL,
    tahun SMALLINT NOT NULL,
    is_weekend BOOLEAN DEFAULT FALSE,
    is_holiday BOOLEAN DEFAULT FALSE
);

CREATE TABLE dim_cabang (
    cabang_id SERIAL PRIMARY KEY,
    cabang_code VARCHAR(10) NOT NULL UNIQUE,
    cabang_name VARCHAR(100) NOT NULL,
    location VARCHAR(150) NOT NULL
);

CREATE TABLE dim_menu (
    menu_id SERIAL PRIMARY KEY,
    menu_code VARCHAR(20) NOT NULL,
    menu_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL
        CHECK (unit_price >= 0),
    effective_from DATE NOT NULL,
    effective_to DATE,
    is_current BOOLEAN DEFAULT TRUE,

    CHECK (
        effective_to IS NULL
        OR effective_to >= effective_from
    )
);

CREATE TABLE dim_porsi (
    porsi_id SERIAL PRIMARY KEY,
    porsi_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(150)
);


-- ============ FACT ============
CREATE TABLE fact_penjualan (
    penjualan_id BIGSERIAL PRIMARY KEY,

    tanggal_id INTEGER NOT NULL,
    cabang_id INTEGER NOT NULL,
    menu_id INTEGER NOT NULL,
    porsi_id INTEGER NOT NULL,

    jumlah_terjual INTEGER NOT NULL
        CHECK (jumlah_terjual > 0),

    harga_satuan NUMERIC(10,2) NOT NULL
        CHECK (harga_satuan >= 0),

    diskon NUMERIC(10,2) DEFAULT 0
        CHECK (diskon >= 0),

    total_penjualan NUMERIC(12,2)
        GENERATED ALWAYS AS
        ((jumlah_terjual * harga_satuan) - diskon) STORED,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_penjualan_tanggal
        FOREIGN KEY (tanggal_id)
        REFERENCES dim_tanggal(tanggal_id),

    CONSTRAINT fk_penjualan_cabang
        FOREIGN KEY (cabang_id)
        REFERENCES dim_cabang(cabang_id),

    CONSTRAINT fk_penjualan_menu
        FOREIGN KEY (menu_id)
        REFERENCES dim_menu(menu_id),

    CONSTRAINT fk_penjualan_porsi
        FOREIGN KEY (porsi_id)
        REFERENCES dim_porsi(porsi_id)
);

-- ============ INDEXES (min 2) ============
CREATE INDEX idx_fact_penjualan_tanggal
ON fact_penjualan(tanggal_id);

CREATE INDEX idx_fact_penjualan_cabang
ON fact_penjualan(cabang_id);

CREATE INDEX idx_fact_penjualan_menu
ON fact_penjualan(menu_id);

CREATE INDEX idx_fact_penjualan_porsi
ON fact_penjualan(porsi_id);
```

---

## Aktivitas 5 — Seed Data & Verifikasi Query

**Seed data (min 10 baris fact):**
```sql
INSERT INTO dim_tanggal
(tanggal_actual, hari_ke, nama_hari, bulan_ke, nama_bulan, tahun, is_weekend, is_holiday)
VALUES
('2026-09-01', 2, 'Selasa', 9, 'September', 2026, FALSE, FALSE),
('2026-09-02', 3, 'Rabu', 9, 'September', 2026, FALSE, FALSE),
('2026-09-03', 4, 'Kamis', 9, 'September', 2026, FALSE, FALSE),
('2026-09-04', 5, 'Jumat', 9, 'September', 2026, FALSE, FALSE),
('2026-09-05', 6, 'Sabtu', 9, 'September', 2026, TRUE, FALSE),
('2026-09-06', 7, 'Minggu', 9, 'September', 2026, TRUE, FALSE);

INSERT INTO dim_cabang
(cabang_code, cabang_name, location)
VALUES
('AF001', 'Mie Ayam Afui Cabang 1', 'Yogyakarta'),
('AF002', 'Mie Ayam Afui Cabang 2', 'Yogyakarta'),
('AF003', 'Mie Ayam Afui Cabang 3', 'Yogyakarta');

INSERT INTO dim_menu
(menu_code, menu_name, category, unit_price, effective_from, effective_to, is_current)
VALUES
('M001', 'Mie Ayam Original', 'Mie Ayam', 15000, '2026-01-01', NULL, TRUE),
('M002', 'Mie Ayam Bakso', 'Mie Ayam', 18000, '2026-01-01', NULL, TRUE),
('M003', 'Mie Ayam Ceker', 'Mie Ayam', 18000, '2026-01-01', NULL, TRUE),
('M004', 'Bakso Kuah', 'Bakso', 16000, '2026-01-01', NULL, TRUE),
('M005', 'Es Teh', 'Minuman', 5000, '2026-01-01', NULL, TRUE);

INSERT INTO dim_porsi
(porsi_name, description)
VALUES
('Biasa', 'Porsi standar'),
('Jumbo', 'Porsi lebih besar');

INSERT INTO fact_penjualan
(tanggal_id, cabang_id, menu_id, porsi_id, jumlah_terjual, harga_satuan, diskon)

SELECT
    d.tanggal_id,
    c.cabang_id,
    m.menu_id,
    p.porsi_id,
    x.jumlah_terjual,
    x.harga_satuan,
    x.diskon

FROM (
    VALUES
        ('2026-09-01', 'AF001', 'M001', 'Biasa', 3, 15000, 0),
        ('2026-09-01', 'AF001', 'M002', 'Biasa', 2, 18000, 0),
        ('2026-09-01', 'AF002', 'M001', 'Biasa', 5, 15000, 2000),
        ('2026-09-02', 'AF002', 'M003', 'Jumbo', 3, 18000, 0),
        ('2026-09-02', 'AF003', 'M001', 'Biasa', 4, 15000, 0),
        ('2026-09-03', 'AF001', 'M004', 'Biasa', 2, 16000, 0),
        ('2026-09-03', 'AF002', 'M002', 'Jumbo', 4, 18000, 3000),
        ('2026-09-04', 'AF003', 'M001', 'Biasa', 6, 15000, 0),
        ('2026-09-05', 'AF001', 'M005', 'Biasa', 8, 5000, 0),
        ('2026-09-05', 'AF002', 'M001', 'Jumbo', 5, 15000, 0),
        ('2026-09-06', 'AF003', 'M002', 'Biasa', 3, 18000, 0),
        ('2026-09-06', 'AF001', 'M003', 'Jumbo', 2, 18000, 1000)
) AS x(
    tanggal,
    kode_cabang,
    kode_menu,
    nama_porsi,
    jumlah_terjual,
    harga_satuan,
    diskon
)

JOIN dim_tanggal d
    ON d.tanggal_actual = x.tanggal::DATE

JOIN dim_cabang c
    ON c.cabang_code = x.kode_cabang

JOIN dim_menu m
    ON m.menu_code = x.kode_menu

JOIN dim_porsi p
    ON p.porsi_name = x.nama_porsi;

```

**Query agregasi contoh (yang berhasil dijalankan):**
```sql

SELECT
    m.menu_name,
    SUM(f.jumlah_terjual) AS total_item_terjual,
    SUM(f.total_penjualan) AS total_penjualan
FROM fact_penjualan f
JOIN dim_menu m
    ON f.menu_id = m.menu_id
GROUP BY m.menu_name
ORDER BY total_penjualan DESC;
```

**Hasil (screenshot/teks):**
```
 Menu              | Total Item Terjual | Total Penjualan |
| ----------------- | -----------------: | --------------: |
| Mie Ayam Original |                 23 |    Rp343.000,00 |
| Mie Ayam Bakso    |                  9 |    Rp159.000,00 |
| Mie Ayam Ceker    |                  5 |     Rp89.000,00 |
| Es Teh            |                  8 |     Rp40.000,00 |
| Bakso Kuah        |                  2 |     Rp32.000,00 |

```

### Catatan Commit
-  Seed 12 baris fact + query agregasi sukses

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
