"""
Program ini digunakan oleh sekretaris kelas untuk merekap kehadiran UTS.
Data disimpan dalam file CSV, dihitung jumlah hadir, lalu diringkas ke file JSON.
"""

from pathlib import Path
import json
import logging

# --- Konfigurasi logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# --- Buat folder data ---
data_presensi = Path("data/presensi.csv")
data_presensi.parent.mkdir(exist_ok=True)

try:
    # --- Tulis data presensi ---
    logging.info("Menulis file presensi.csv...")
    with data_presensi.open("w") as data:
        data.write("230103195, himas, 1\n")
        data.write("230103196, budi, 0\n")
        data.write("230103197, siti, 1\n")
    logging.info("File presensi.csv berhasil dibuat.")

    # --- Baca data presensi ---
    logging.info("Membaca file presensi.csv...")
    with data_presensi.open("r") as data:
        lines = data.readlines()

    total = len(lines)
    hadir = 0
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) == 3 and parts[2] == "1":
            hadir += 1

    persentase = (hadir / total) * 100 if total > 0 else 0

    # --- Cetak hasil ---
    print(f"Total data   : {total}")
    print(f"Hadir        : {hadir}")
    print(f"Persentase   : {persentase:.2f}%")

    # --- Simpan hasil ke JSON ---
    ringkasan = {
        "total": total,
        "hadir": hadir,
        "persentase": round(persentase, 2)
    }

    data_ringkasan = Path("data/ringkasan.json")

    logging.info("Menyimpan ringkasan ke ringkasan.json...")
    with data_ringkasan.open("w") as file_json:
        json.dump(ringkasan, file_json, indent=4)
    logging.info("Ringkasan berhasil disimpan ke data/ringkasan.json.")

except Exception as e:
    logging.error(f"Terjadi kesalahan: {e}")
