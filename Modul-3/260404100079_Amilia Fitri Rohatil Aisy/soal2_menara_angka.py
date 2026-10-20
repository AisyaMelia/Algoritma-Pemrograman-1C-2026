n = int(input("Tinggi (2-15): "))
while n < 2 or n > 15:
    n = int(input("Tidak valid, ulangi (2-15): "))

for b in range(1, 2 * n):
    i = b if b <= n else 2 * n - b      # naik sampai n, lalu turun
    baris = " " * (n - i)
    for k in range(1, i + 1):
        baris += str(k % 10)
    for k in range(i - 1, 0, -1):
        baris += str(k % 10)
    print(baris)
