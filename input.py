#tambah
namadepan = input("Nama depan Anda siapa? ")
namabelakang = input("Nama belakang Anda siapa? ")
print("Seluruh karakter =", namabelakang)
print("Karakter ke sekian (start index 0) =", namabelakang[2])
print("Karakter ke sekian sampai sekian (start index 0) =", namabelakang[2:6])
print("Panjang karakter =", len(namabelakang))
namalengkap = namadepan + " " + namabelakang
print("Nama lengkap anda adalah =", namalengkap)

#pake format
usia = 38
print("Usia saya adalah {}".format(usia))
#pake f
usiananti = 40
printusia = f"Usia saya adalah {usia}, 2 tahun lagi {usiananti}"
print(printusia)