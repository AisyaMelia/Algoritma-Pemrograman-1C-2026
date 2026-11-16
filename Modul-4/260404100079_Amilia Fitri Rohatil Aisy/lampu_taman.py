jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for baris in range(1, jumlah_baris):
    print("baris", baris)
    for lampu in range(1, jumlah_lampu):
        if lampu % 3 == 0:
            print("  Lampu", lampu, ": mengalami gangguan")
        else:
            print("  Lampu", lampu, ": berfungsi normal")

print("Semua lampu sudah diperiksa.")
print("Silakan periksa sumber listrik utama taman!")
