#pendaftaran anggota klub robotika
daftar_nama = []

#input nama terus-menerus sampai ketik "selesai"
while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar_nama.append(nama)

#periksa satu per satu dari awal sampai akhir
print("\n--- Hasil Pemeriksaan ---")
for nama in daftar_nama:
    if nama == "admin" or len(nama) < 4:
        print("Nama", nama, "tidak valid!")
    else:
        print("Nama", nama, "valid")

#hapus nama penyusup (aman, tidak crash kalau tidak ada)
penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in daftar_nama:
    daftar_nama.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus.")
else:
    print("Nama", penyusup, "tidak ditemukan di pendaftaran.")

print("\nDaftar nama sekarang:", daftar_nama)
