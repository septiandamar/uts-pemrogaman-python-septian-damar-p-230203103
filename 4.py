def jadwal_hari(hari):
    jadwal = {
        "Senin": ["Algoritma", "Basis Data"],
        "Selasa": ["Python", "Jaringan"],
        "Rabu": ["Sistem Operasi"],
        "Kamis": ["Web", "Pancasila"],
        "Jumat": ["Analisis Sistem"]
    }

    if hari in jadwal:
        print(f"Jadwal {hari}: {', '.join(jadwal[hari])}")
    else:
        print("Hari tidak ditemukan")

# Contoh penggunaan
jadwal_hari("Selasa")
