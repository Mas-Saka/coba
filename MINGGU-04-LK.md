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
<Query digunakan untuk mengetahui peringkat menu berdasarkan jumlah item yang terjual pada masing-masing cabang Mie Ayam Afui. Fungsi RANK() digunakan untuk memberikan peringkat menu di dalam setiap cabang. Dengan hasil tersebut, pengelola dapat mengetahui menu yang paling banyak terjual pada setiap cabang dan membandingkan pola penjualan antar-cabang.

Query ini menggunakan PARTITION BY berdasarkan cabang sehingga peringkat dimulai kembali dari setiap cabang>

## Aktivitas 2 — EXPLAIN ANALYZE
> Tempel ringkasan plan (Index Scan / Seq Scan, actual time) + analisis singkat.
- Jenis scan: <...>
- Analisis: <perlu index? mengapa?>

## Aktivitas 3 — Information-gap (refleksi)
- Query yang paling sulit disatukan saat pairing: <...>
- Pelajaran yang didapat: <...>

## Refleksi Pribadi Per Anggota
> Wajib masing-masing anggota (1-2 paragraf). 

### [Isyaka Dhafa Maulana — Ketua]
<refleksi >

### [Habrian Daffa Dwiyandana - Anggota 2]
<refleksi>

### [Mohamad Safi'i - Anggota 3]
<refleksi>

### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]
<refleksi>

### [Embun Bigar Hidayat - Anggota 5]
<refleksi>

## Checklist
- [ ] 1 query window/CTE + maksud bisnis
- [ ] EXPLAIN ringkas + analisis
- [ ] Refleksi information-gap
- [ ] Refleksi anggota

```
**Maksud bisnis:** <Query digunakan untuk mengetahui peringkat menu berdasarkan jumlah item yang terjual pada masing-masing cabang Mie Ayam Afui. Fungsi RANK() digunakan untuk memberikan peringkat menu di dalam setiap cabang. Dengan hasil tersebut, pengelola dapat mengetahui menu yang paling banyak terjual pada setiap cabang dan membandingkan pola penjualan antar-cabang.

Query ini menggunakan PARTITION BY berdasarkan cabang sehingga peringkat dimulai kembali dari setiap cabang>

## Aktivitas 2 — EXPLAIN ANALYZE
> Tempel ringkasan plan (Index Scan / Seq Scan, actual time) + analisis singkat.
- Jenis scan: <...>
- Analisis: <perlu index? mengapa?>

## Aktivitas 3 — Information-gap (refleksi)
- Query yang paling sulit disatukan saat pairing: <...>
- Pelajaran yang didapat: <...>

## Refleksi Pribadi Per Anggota
> Wajib masing-masing anggota (1-2 paragraf). 

### [Isyaka Dhafa Maulana — Ketua]
<refleksi >

### [Habrian Daffa Dwiyandana - Anggota 2]
<refleksi>

### [Mohamad Safi'i - Anggota 3]
<refleksi>

### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]
<refleksi>

### [Embun Bigar Hidayat - Anggota 5]
<refleksi>

## Checklist
- [ ] 1 query window/CTE + maksud bisnis
- [ ] EXPLAIN ringkas + analisis
- [ ] Refleksi information-gap
- [ ] Refleksi anggota
