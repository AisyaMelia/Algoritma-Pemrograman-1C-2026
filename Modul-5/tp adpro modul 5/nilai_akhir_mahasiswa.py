def hitung_nilai(nama, tugas, uts, uas):
    #bobot: tugas 30%, UTS 30%, UAS 40%
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    #tentukan grade
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    #tentukan status kelulusan
    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    #tampilkan hasil lengkap
    print()
    print("------ HASIL NILAI AKHIR ------")
    print("Nama mahasiswa :", nama)
    print("Nilai tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Status         :", status)


print()
print("=== SOAL 3: NILAI AKHIR MAHASISWA ===")
nama_mhs = input("Masukkan nama mahasiswa : ")
nilai_tugas = float(input("Masukkan nilai tugas : "))
nilai_uts = float(input("Masukkan nilai UTS   : "))
nilai_uas = float(input("Masukkan nilai UAS   : "))

hitung_nilai(nama_mhs, nilai_tugas, nilai_uts, nilai_uas)