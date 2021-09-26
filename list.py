# x = 15
# y = "Usia ="
# var_list = [x,y]

# print(var_list[1],var_list[0])

var_list2 = []
isi1 = input("Angka 1 = ")
isi2 = input("Angka 2 = ")
isi3 = input("Angka 3 = ")
var_list2.append(isi1) #append masuk datanya di index terakhir
var_list2.append(isi3)
var_list2.insert(1,isi2) #insert masuk data sesuai pilihan
print("Angka 1 = ", var_list2[0],"Angka 2 = ", var_list2[1],"Angka 3 = ", var_list2[2])

#loop pake for
for x in var_list2:
    print(x)