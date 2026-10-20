jumlah = total = total_jarak = terjauh = 0

while True:
    jarak = int(input("Jarak (0 = selesai): "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    jumlah += 1
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
    if jumlah % 5 == 0:
        tarif /= 2          # diskon 50%

    print("Tarif:", tarif)
    total += tarif
    total_jarak += jarak
    terjauh = max(terjauh, jarak)

print("Penumpang:", jumlah)
print("Pendapatan:", total)
print("Jarak terjauh:", terjauh)
if jumlah > 0:
    print("Rata-rata jarak:", total_jarak / jumlah)
