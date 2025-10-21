def jadwal_hari(hari):
    jadwal = {
        "senin": ["08:00 Pemrograman", "10:00 Matematika Diskrit"],
        "selasa": ["09:00 Basis Data", "13:00 Sistem Operasi"],
        "rabu": ["08:00 Jaringan Komputer"],
        "kamis": ["10:00 Praktikum Python"],
        "jumat": ["09:00 Etika Profesi"]
    }

    hari = hari.lower()  # supaya input "Senin" cocok dengan "senin"

    if hari in jadwal:
        print(f"Jadwal hari {hari.title()}:")
        for mata_kuliah in jadwal[hari]:
            print("-", mata_kuliah)
    else:
        print("Tidak ada jadwal untuk hari tersebut.")


hari_input = input("Masukkan hari: ")
jadwal_hari(hari_input)
