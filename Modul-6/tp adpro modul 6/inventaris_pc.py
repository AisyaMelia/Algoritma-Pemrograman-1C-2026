#inventaris PC (list multidimensi)

#fungsi kustom untuk cek kelayakan PC
#sengaja TIDAK ada validasi, jadi kalau RAM berupa teks akan error
def cek_kelayakan(data_pc):
    status = data_pc[1]
    ram = int(data_pc[2])          #error jika isinya 'Delapan'
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

#input data PC (tanpa validasi tipe data)
jumlah = int(input("Masukkan jumlah PC: "))

inventaris = []          #list multidimensi (list di dalam list)
for i in range(jumlah):
    print("\nPC ke-" + str(i + 1))
    nama = input("Nama PC             : ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB)   : ")          #dibiarkan apa adanya (string)
    inventaris.append([nama, status, ram])

#evaluasi semua PC
print("\n--- Hasil Evaluasi ---")
for pc in inventaris:
    try:
        hasil = cek_kelayakan(pc)
    except ValueError:
        hasil = "Format RAM Kacau"

    #cetak dengan manipulasi string
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')
