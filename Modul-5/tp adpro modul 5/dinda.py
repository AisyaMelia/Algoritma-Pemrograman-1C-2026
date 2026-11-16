def cek_palindrom(kata):
    #ubah ke huruf kecil supaya tidak membedakan besar/kecil
    kata = kata.lower()
    #kata[::-1] artinya kata dibaca dari belakang
    if kata == kata[::-1]:
        return True
    else:
        return False


print()
print("=== SOAL 2: PALINDROM ===")
kata_input = input("Masukkan sebuah kata : ")

hasil_palindrom = cek_palindrom(kata_input)
print("Hasil fungsi :", hasil_palindrom)

if hasil_palindrom == True:
    print("Kata", kata_input, "adalah PALINDROM")
else:
    print("Kata", kata_input, "BUKAN palindrom")