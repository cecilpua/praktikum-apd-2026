batas = 5 
for i in range(batas):
    print("Perulangan ke-", i)

game = ["Genshin", 7.0, True]
for i in game:
    print(i)

for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('')

jawab = "ya"
hitung = 0

while(jawab == "ya"):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total Perulangan : {hitung}")

#kontrol perulangan (break)
for i in range(10):
    if i == 5:
        break
print(i)

#(Continue)
for i in range(10):
    if i % 2 == 0:
        continue
print(i)