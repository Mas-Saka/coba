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
┌─────────────────────┐             │             ┌─────────────────────┐
│     DIM_MENU        │             │             │    DIM_CABANG       │
├─────────────────────┤             │             ├─────────────────────┤
│ PK menu_key         │             │             │ PK cabang_key       │
│ nama_menu           │             │             │ nama_cabang         │
│ kategori            │             │             │ lokasi              │
│ harga               │             │             └──────────┬──────────┘
└──────────┬──────────┘             │                        │
           │                        │                        │
           │                        │                        │
           └────────────────────────┼────────────────────────┘
                                    │
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     FACT_PENJUALAN  │
                         ├─────────────────────┤
                         │ PK penjualan_key    │
                         │ FK tanggal_key      │
                         │ FK menu_key         │
                         │ FK cabang_key       │
                         │ jumlah_terjual      │
                         │ total_penjualan     │
                         │ harga_satuan        │
                         └─────────────────────┘
