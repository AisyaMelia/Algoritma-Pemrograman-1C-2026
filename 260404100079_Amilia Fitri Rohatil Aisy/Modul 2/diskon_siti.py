total = int(input("Masukkan total belanja (Rp): "))
print("Total belanja awal: Rp", total)

# Diseleksi berurutan dari promo terbesar ke terkecil (hanya satu yang berlaku)
if total % 100000 == 0:
    bayar = 0
    print("Promo: Gratis seluruh belanjaan")
elif total % 50000 == 0:
    bayar = total * 50 // 100
    print("Promo: Diskon 50%")
elif total % 10000 == 0:
    bayar = total * 80 // 100
    print("Promo: Diskon 20%")
elif total >= 200000:
    bayar = total * 90 // 100
    print("Promo: Diskon 10%")
else:
    bayar = total
    print("Promo: Tidak ada, bayar harga normal")

print("Total harga akhir yang dibayar: Rp", bayar)

# Ternary operator
poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin keanggotaan:", poin)
