def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung ongkir berdasarkan kota, berat, dan asuransi."""
    tarif_dasar = {"Sragen": 10000, "ngawi": 12000, "Surabaya": 15000}
    ongkir = tarif_dasar.get(kota, 0) + 2000 * berat_kg
    if asuransi:
        ongkir += 3000
    return ongkir


# Contoh pemanggilan:
print(hitung_ongkir(2, "Sragen"))
print(hitung_ongkir(3, "Surabaya", True))