# Lembar Kerja Mahasiswa (LK) — Pertemuan 7
## Tugas 5: Interactive Dashboard Development (DAX + fitur lanjutan)

> **PETUNJUK:** Copy ke `kel-XX/minggu-07/LK.md`. Lanjutan prototype minggu 6.
> Commit min 10x. Screenshot + formula DAX tertulis.

## Identitas
| Field | Isi |
|---|---|
| Kelas |  SI-C |
| Kelompok | 06 |
| Sub-CPMK | Sub-CPMK03 — Interactive Dashboard |
| Bobot | 2% (Tugas 5) |

## Aktivitas 1 — Measure DAX (min 3, sebut formula)
1. `Total Revenue := SUM(fact_sales[amount])`
2. `<nama measure>` := `<formula DAX>`
3. `<nama measure>` := `<formula DAX>`

## Aktivitas 2 — Interaktivitas (min slicer + 1 fitur)
- **Slicer:** <apa, mis. tanggal / cabang>
- **Drill-through / Bookmark / Tooltip:** <pilih satu, jelaskan cara pakai & apa yang dijawab>

## Aktivitas 3 — Alur Interaksi Pengguna
> Jelaskan langkah pengguna menjelajah dashboard (mis. "pilih cabang A di slicer
> → lihat tren → klik menu terlaris → drill-through ke detail transaksi").
<alur>

Diagram Alur Interaksi Pengguna
+--------------------------+
| Membuka Dashboard Utama  |
+--------------------------+
            |
            v
+--------------------------+
| Melihat Ringkasan KPI    |
+--------------------------+
            |
            v
+--------------------------+
| Memilih Filter Slicer    |
| Tahun, Kategori, Cabang  |
+--------------------------+
            |
            v
+--------------------------+
| Mengamati Visualisasi    |
| Penjualan                |
+--------------------------+
            |
            v
+--------------------------+
| Memilih Data Menu        |
+--------------------------+
            |
            v
+--------------------------+
| Menggunakan Drill-through|
+--------------------------+
            |
            v
+--------------------------+
| Melihat Detail Penjualan |
+--------------------------+
            |
            v
+--------------------------+
| Kembali ke Dashboard     |
+--------------------------+
**Screenshot dashboard interaktif:** 
<dashboardutama.png>

## Aktivitas 4 — (Bonus) Row-Level Security
- Role: <nama> — filter DAX: <`[outlet_code]="A"`>
- Uji: <hasil saat masuk sebagai user lain>

## Refleksi Pribadi Per Anggota
### [Isyaka Dhafa Maulana — Ketua]
<refleksi: interaksi mana paling berguna untuk audience? ada yang justru membingungkan?>


### [Habrian Daffa Dwiyandana - Anggota 2]
<refleksi: interaksi mana paling berguna untuk audience? ada yang justru membingungkan?>


### [Mohamad Safi'i - Anggota 3]
<refleksi: interaksi mana paling berguna untuk audience? ada yang justru membingungkan?>


### [Muhammad Irfan Mukasyaf Al Fuady - Anggota 4]
<refleksi: interaksi mana paling berguna untuk audience? ada yang justru membingungkan?>


### [Embun Bigar Hidayat - Anggota 5]
<refleksi: interaksi mana paling berguna untuk audience? ada yang justru membingungkan?>


## Daftar Kontribusi
| Anggota | Bagian yang Dikerjakan | Persentase Kontribusi |
|---|---|---|
| Isyaka Dhafa Maulana |  | % |
| Habrian Daffa Dwiyandana |  | % |
| Mohamad Safi'i |  | % |
| Muhammad Irfan Mukasyaf Al Fuady | | % |
| Embun Bigar Hidayat |  | % |
| **Total** | | **100%** |

## Checklist
- [ ] >=3 measure DAX + formula
- [ ] Slicer + 1 fitur interaktif (drill/bookmark/tooltip)
- [ ] Alur interaksi dijelaskan + screenshot
- [ ] (Bonus) RLS role
- [ ] Refleksi anggota + kontribusi 100%
- [ ] >=10 commit
