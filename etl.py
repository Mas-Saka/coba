import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


def extract(file_path):
    print("Memulai proses Extract...")

    df = pd.read_csv(file_path)

    print("Jumlah data yang dibaca:", len(df))

    return df


def transform(df):
    print("Memulai proses Transform...")

    # Menghapus data duplikat
    df = df.drop_duplicates()

    # Membersihkan data teks
    df["kode_cabang"] = df["kode_cabang"].astype(str).str.strip()
    df["kode_menu"] = df["kode_menu"].astype(str).str.strip()
    df["nama_porsi"] = df["nama_porsi"].astype(str).str.strip()

    # Mengubah tipe tanggal
    df["tanggal"] = pd.to_datetime(df["tanggal"])

    # Mengubah kolom numerik
    df["jumlah_terjual"] = pd.to_numeric(
        df["jumlah_terjual"],
        errors="coerce"
    )

    df["harga_satuan"] = pd.to_numeric(
        df["harga_satuan"],
        errors="coerce"
    )

    # Diskon kosong dianggap 0
    df["diskon"] = df["diskon"].fillna(0)

    df["diskon"] = pd.to_numeric(
        df["diskon"],
        errors="coerce"
    )

    print("Jumlah data setelah transform:", len(df))

    return df


def validate(df):
    print("Memulai proses Validasi...")

    required_columns = [
        "tanggal",
        "kode_cabang",
        "kode_menu",
        "nama_porsi",
        "jumlah_terjual",
        "harga_satuan"
    ]

    # Completeness
    assert df[required_columns].notnull().all().all(), \
        "Terdapat data wajib yang kosong"

    # Validity
    assert (df["jumlah_terjual"] > 0).all(), \
        "Terdapat jumlah terjual tidak valid"

    assert (df["harga_satuan"] >= 0).all(), \
        "Terdapat harga satuan negatif"

    assert (df["diskon"] >= 0).all(), \
        "Terdapat diskon negatif"

    # Uniqueness
    assert df.duplicated().sum() == 0, \
        "Masih terdapat data duplikat"

    print("Validasi data berhasil")


def load(df):
    print("Memulai proses Load...")

    conn = psycopg2.connect(
        host="localhost",
        database="mie_ayam",
        user="postgres",
        password="sdms1234",
        port="5432"
    )

    cur = conn.cursor()

    # Mengambil tanggal_id
    cur.execute("""
        SELECT tanggal_id, tanggal_actual
        FROM dim_tanggal
    """)

    dim_tanggal = cur.fetchall()

    tanggal_map = {}

    for row in dim_tanggal:
        tanggal_map[row[1]] = row[0]

    # Mengambil cabang_id
    cur.execute("""
        SELECT cabang_id, cabang_code
        FROM dim_cabang
    """)

    dim_cabang = cur.fetchall()

    cabang_map = {}

    for row in dim_cabang:
        cabang_map[row[1]] = row[0]

    # Mengambil menu_id
    cur.execute("""
        SELECT menu_id, menu_code
        FROM dim_menu
        WHERE is_current = TRUE
    """)

    dim_menu = cur.fetchall()

    menu_map = {}

    for row in dim_menu:
        menu_map[row[1]] = row[0]

    # Mengambil porsi_id
    cur.execute("""
        SELECT porsi_id, porsi_name
        FROM dim_porsi
    """)

    dim_porsi = cur.fetchall()

    porsi_map = {}

    for row in dim_porsi:
        porsi_map[row[1]] = row[0]

    # Menambahkan surrogate key
    df["tanggal_id"] = df["tanggal"].dt.date.map(tanggal_map)
    df["cabang_id"] = df["kode_cabang"].map(cabang_map)
    df["menu_id"] = df["kode_menu"].map(menu_map)
    df["porsi_id"] = df["nama_porsi"].map(porsi_map)

    # Consistency
    assert df["tanggal_id"].notnull().all(), \
        "Terdapat tanggal yang tidak ditemukan di dim_tanggal"

    assert df["cabang_id"].notnull().all(), \
        "Terdapat cabang yang tidak ditemukan di dim_cabang"

    assert df["menu_id"].notnull().all(), \
        "Terdapat menu yang tidak ditemukan di dim_menu"

    assert df["porsi_id"].notnull().all(), \
        "Terdapat porsi yang tidak ditemukan di dim_porsi"

    # Menentukan periode data
    start_date = df["tanggal"].min().date()
    end_date = df["tanggal"].max().date()

    print("Periode ETL:", start_date, "sampai", end_date)

    # Delete-then-insert untuk idempotensi
    cur.execute("""
        DELETE FROM fact_penjualan
        WHERE tanggal_id IN (
            SELECT tanggal_id
            FROM dim_tanggal
            WHERE tanggal_actual BETWEEN %s AND %s
        )
    """, (start_date, end_date))

    # Menyiapkan data fact
    data_fact = []

    for _, row in df.iterrows():
        data_fact.append((
            int(row["tanggal_id"]),
            int(row["cabang_id"]),
            int(row["menu_id"]),
            int(row["porsi_id"]),
            int(row["jumlah_terjual"]),
            float(row["harga_satuan"]),
            float(row["diskon"])
        ))

    # Bulk insert
    query = """
        INSERT INTO fact_penjualan
        (
            tanggal_id,
            cabang_id,
            menu_id,
            porsi_id,
            jumlah_terjual,
            harga_satuan,
            diskon
        )
        VALUES %s
    """

    execute_values(
        cur,
        query,
        data_fact
    )

    conn.commit()

    print("Jumlah data berhasil dimuat:", len(data_fact))

    cur.close()
    conn.close()


def run_etl(file_path):
    print("========== ETL DIMULAI ==========")

    df = extract(file_path)

    df = transform(df)

    validate(df)

    load(df)

    print("========== ETL SELESAI ==========")


if __name__ == "__main__":
    run_etl(r"D:\Isyaka\Tugas Kuliah\kecerdasan-bisnis-si-c-2026-2027\kel-06\minggu-04\data_transaksi_mie_ayam_afui.csv")