listnama = []
listtelepon = []

while True:
    print("\n===========================\n")
    print("Selamat Datang!")
    print("\n--Menu--\n")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = int(input("\nSilakan pilih menu yang anda inginkan = "))

    if pilihan == 1:
        print("\n===========================")
        for x in listnama:
            for y in listtelepon:
                if listnama.index(x) == listtelepon.index(y):
                    print("\nNama : ",x)
                    print("No. Telepon :",y)
    elif pilihan == 2:
        nama = input("Nama : ")
        listnama.append(nama)
        telepon = input("No. Telepon : ")
        listtelepon.append(telepon)
    elif pilihan == 3:
        print("\n===========================\n")
        print("Program selesai, sampai jumpa!")
        print("\n===========================\n")
        break
    else:
        print("\n===========================\n")
        print("Menu tidak tersedia")
        print("\n===========================\n")


# nama = input("Nama 1 = ")
# umur = input("Nama 2 = ")
# tinggi = input("Nama 3 = ")
# y = range(3)
# for nama in range(3):
#     nama = input("Nama = ")
#     listnama.append(nama)

# for x in listnama:
#     print(x)
# i = 0
# while i < 3:
#     nama = input("Nama = ")
#     listnama.append(nama)
#     i = i + 1
# for x in listnama:
#     print(x)