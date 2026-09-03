## Arsitektur Business Intelligence

```text
┌─────────────────────────────────────────────────────────────────┐
│  1. SOURCE DATA                                                 │
│                                                                 │
│  Cabang 1        Cabang 2        Cabang 3                      │
│      │               │               │                          │
│      └─────── Data Transaksi / POS / CSV ────────┘             │
│                                                                 │
│  • Data transaksi                                               │
│  • Data menu                                                    │
│  • Data porsi                                                   │
│  • Data cabang                                                  │
│  • Data tanggal/waktu                                           │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. INGESTION / ETL                                             │
│                                                                 │
│                    Python + Pandas                              │
│                                                                 │
│  Extract → Cleaning → Transformation → Validation → Load       │
│                                                                 │
│  • Standardisasi kode menu                                      │
│  • Standardisasi kode cabang                                   │
│  • Validasi transaksi                                           │
│  • Penanganan data kosong/duplikat                              │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. STORAGE                                                     │
│                                                                 │
│                       PostgreSQL                                │
│                                                                 │
│                       STAR SCHEMA                               │
│                                                                 │
│                       ┌───────────────┐                         │
│                       │ FACT PENJUALAN│                         │
│                       └───────┬───────┘                         │
│                               │                                 │
│          ┌────────────────────┼────────────────────┐            │
│          │                    │                    │            │
│     DIM MENU             DIM TANGGAL          DIM CABANG       │
│          │                    │                    │            │
│     DIM PORSI               ...                  ...            │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. SEMANTIC / MODELING                                         │
│                                                                 │
│                  SQL VIEW / POWER BI MODEL                      │
│                                                                 │
│  Measures:                                                      │
│  • Total Penjualan                                              │
│  • Jumlah Transaksi                                             │
│  • Jumlah Item Terjual                                          │
│  • Rata-rata Nilai Transaksi                                    │
│                                                                 │
│  Analisis:                                                      │
│  • Cabang                                                       │
│  • Menu                                                         │
│  • Porsi                                                        │
│  • Hari / Bulan / Tahun                                         │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. PRESENTATION                                                │
│                                                                 │
│                         POWER BI                                │
│                                                                 │
│  Dashboard Utama                                                │
│  ├── Perbandingan performa 3 cabang                             │
│  ├── Menu terlaris                                              │
│  ├── Tren penjualan                                             │
│  ├── Penjualan per cabang                                       │
│  └── Penjualan berdasarkan porsi                                │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  6. METADATA & GOVERNANCE                                       │
│                                                                 │
│  • Access Control                                               │
│  • Data Quality                                                 │
│  • Backup                                                       │
│  • Metadata                                                     │
│  • Data Lineage                                                 │
│  • Standardisasi data cabang dan menu                            │
│  • Audit akses                                                  │
└─────────────────────────────────────────────────────────────────┘
```
