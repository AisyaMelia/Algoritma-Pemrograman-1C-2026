gaji_pokok = 100000
total_gaji = 0

for hari in range(1, 8):
    print("=== Hari ke-" + str(hari) + " ===")

    #jam lembur: sampai input sesuai ketentuan
    while True:
        lembur = int(input("Jam lembur (0/1/2/3/4/6/8): "))
        if lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan! Input ulang.")
        elif lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("Jam lembur tidak sesuai ketentuan! Input ulang.")

    shift = input("Shift malam? (y/t): ")

    #tentukan upah lembur
    if lembur == 0:
        upah_lembur = 0
    elif lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    else:  # lembur == 8
        upah_lembur = 300000

    # Tambahan shift malam
    if shift == "y":
        tambahan = 50000
    else:
        tambahan = 0

    gaji_hari = gaji_pokok + upah_lembur + tambahan
    total_gaji = total_gaji + gaji_hari
    print("Gaji hari ke-" + str(hari) + ": Rp", gaji_hari)

print("Total gaji mingguan: Rp", total_gaji)
