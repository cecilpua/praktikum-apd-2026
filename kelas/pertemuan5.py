kartu = {"merah", "merah", "biru", "hijau"}

kartu.add("hytam")

kartu.remove("green")
kartu.discard("red")

print(kartu)

matkul = ("apd", "orsikom", "apd", "kalkulus")

sks = set(matkul)
print(sks)

angka_ganjil = {1, 3, 5, 7, 9}
for angka in angka_ganjil:
    print (angka)

aslab1 = {"fina", "shasha", "risma"}
aslab2 = {"larry", "attar", "haekal"}

gabung = aslab1.union(aslab2)
print(gabung)

Matkul = {
    "Matkul_ganjil" : "kalkulus",
"Matkul_genap" : "statistik"
}
print(Matkul["Matkul_ganjil"])
print(Matkul)


game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

for i in game:
    print(i)
for i in game.keys():
    print(i)

game = {
"pou" : "chill",
"genshin impact" : "action","valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

game["resident evil"] = "horror"
print(game)