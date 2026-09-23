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
<...>

## Aktivitas 2 — EXPLAIN ANALYZE
> Tempel ringkasan plan (Index Scan / Seq Scan, actual time) + analisis singkat.
- fact_penjualan: Seq Scan, dengan actual time=0.016..0.018 ms, membaca 12 baris. Data difilter menggunakan tanggal_id antara 1 sampai 6.
- dim_menu: Seq Scan, dengan actual time=0.047..0.048 ms, membaca 5 baris.
- Join: PostgreSQL menggunakan Hash Join dengan kondisi m.menu_id = f.menu_id untuk menggabungkan data dari dim_menu dan fact_penjualan.
- Agregasi: HashAggregate digunakan untuk mengelompokkan data berdasarkan menu_name dan menghasilkan 5 baris.
- sort : hasil agregasi diurutkan berdasarkan SUM(f.jumlah_terjual) secara menurun menggunakan metode quicksort dengan penggunaan memori 25 kB.
- Planning Time: 0.347 ms.
- Execution Time: 0.742 ms.
- Jenis scan: <...>
- Analisis: <...>

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
