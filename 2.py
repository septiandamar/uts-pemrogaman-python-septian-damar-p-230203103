s1 = float (input("masukan setoran 1: "))
s2 = float (input("masukan setoran 2: "))
s3 = float (input("masukan setoran 3: "))

if s1<= 0 or s2<= 0 or s3<= 0 :
    print("input tidak valid")
else :
    total = s1 + s2 + s3
    if total <300000:
        kategori = "rendah" 
    elif total <600000:
        kategori = "sedang"
    else :
        kategori = "tinggi"
    print(f"total :{total}, kategori : {kategori}")