#Statis
jarak = 100 #km
tingkat_bbm = 40 #km/liter
sisa_bbm = 1.5 #liter
harga_bbm_perliter = 10000 #Rp/liter

#Perhitungan
total_jarak = jarak * 2
print("total jarak =", total_jarak)

total_kebutuhan_bbm = total_jarak / tingkat_bbm
print("total kebutuhan bbm =", total_kebutuhan_bbm)

bbm_harus_dibeli = max(0.0, total_kebutuhan_bbm - sisa_bbm)
print("bbm yang harus dibeli =", bbm_harus_dibeli)

total_biaya = bbm_harus_dibeli * harga_bbm_perliter
print("total biaya =", total_biaya)
