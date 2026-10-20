jumlah = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
total = 0
tinggi, rendah = -1, 101

for i in range(10):
    nama = input("Nama: ")
    tugas = float(input("Tugas: "))
    uts = float(input("UTS: "))
    uas = float(input("UAS: "))
    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        k = "A"
    elif akhir >= 75:
        k = "B"
    elif akhir >= 65:
        k = "C"
    elif akhir >= 50:
        k = "D"
    else:
        k = "E"

    jumlah[k] += 1
    total += akhir
    print(nama, tugas, uts, uas, "Akhir:", akhir, "Kategori:", k)

    if akhir > tinggi:
        tinggi, n_tinggi = akhir, nama
    if akhir < rendah:
        rendah, n_rendah = akhir, nama

print("Jumlah per kategori:", jumlah)
print("Tertinggi:", tinggi, n_tinggi)
print("Terendah:", rendah, n_rendah)
print("Rata-rata:", total / 10)
