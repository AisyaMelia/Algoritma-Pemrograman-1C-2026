#penjadwalan shift asisten laboratorium

#pertama: asisten awal, lalu dikunci jadi tuple
list_asisten = []
while True:
    nama = input("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    list_asisten.append(nama)

asisten_awal = tuple(list_asisten)          #tuple tidak bisa diubah (terkunci)

#kedua: tambah 1 asisten baru, gabung ke tuple baru
asisten_tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (asisten_tambahan,)          #tanda koma penting!

#ketiga: hari tugas, lalu dikunci jadi tuple
list_hari = []
while True:
    hari = input("Masukkan nama hari tugas (ketik 'cukup' untuk berhenti): ")
    if hari == "cukup":
        break
    list_hari.append(hari)

hari_tugas = tuple(list_hari)

#pengecualian
asisten_libur = input("Masukkan nama asisten yang dikecualikan: ")
hari_libur = input("Masukkan hari pengecualiannya: ")

#pasangkan setiap asisten dengan setiap hari
print("\n--- Jadwal Shift ---")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == asisten_libur and hari == hari_libur:
            continue          #lewati kombinasi pengecualian
        print(asisten, "-", hari)
