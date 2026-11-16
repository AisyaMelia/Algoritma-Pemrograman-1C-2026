def pelanggan(n):
    #basis: hari ke-1 dan ke-2 jumlahnya 1 orang
    if n == 1 or n == 2:
        return 1
    #rekursif: jumlah hari ini = jumlah 2 hari sebelumnya dijumlahkan
    return pelanggan(n - 1) + pelanggan(n - 2)


print("=== PELANGGAN BU LASTRI ===")
N = int(input("Masukkan hari ke-N (bilangan bulat positif) : "))
if N <= 0:
    print("Input salah! N harus bilangan bulat positif.")
else:
    hasil = pelanggan(N)
    print("Jumlah pelanggan pada hari ke-" + str(N), "adalah", hasil, "orang")