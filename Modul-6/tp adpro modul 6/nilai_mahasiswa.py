nilai = {}

n = int(input("Jumlah mahasiswa: "))

for i in range(n):
    nama = input(f"Nama mahasiswa ke-{i+1}: ")
    skor = int(input(f"Nilai tugas {nama}: "))
    nilai[nama] = skor

# 1. keys() -> daftar nama
print()
for nama in nilai.keys():
    print(nama, end=" ")
print()

# 2. values() -> total nilai
print("Total:", sum(nilai.values()))

# 3. items() -> nama -> nilai
for nama, skor in nilai.items():
    print(f"{nama:5} -> {skor}")