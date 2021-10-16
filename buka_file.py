# file_x = "test.txt"
# file_x.write = 

# with open("folder/test.txt", "r") as filex:
#     print(filex.readlines())

# import os
# os.remove("test.txt")

# import mymodule

# print("PI:",mymodule.pi)
# print(mymodule.luas_persegi(12))

with open("send_email/list_email.txt", "r") as filex:
    penerima = filex.readlines()

# for x in range(len(penerima)):
#     y = penerima[x].split("@")[0]
#     print(f"penerima ke {x+1} = {y}")

for x in range(len(penerima)):
    indeks_at = penerima[x].index('@')
    receiver = penerima[x][0:indeks_at]
    print(receiver)