skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

ongkir = 12000

total_pengeluaran = (
    skincare_1
    + skincare_2
    + skincare_3
    + skincare_4
    + skincare_5
    + skincare_6
    + ongkir
)

daftar_item = [
    skincare_1,
    skincare_2,
    skincare_3,
    skincare_4,
    skincare_5,
    skincare_6,
    ongkir,
]
banyak_data = len(daftar_item)

rata_rata = total_pengeluaran / banyak_data

nim = 25

bolean = nim < rata_rata

print("Skincare 1:", skincare_1)
print("Skincare 2:", skincare_2)
print("Skincare 3:", skincare_3)
print("Skincare 4:", skincare_4)
print("Skincare 5:", skincare_5)
print("Skincare 6:", skincare_6)
print("Ongkos Kirim:", ongkir)
print("Total Pengeluaran:", total_pengeluaran)
print("Rata-rata Pengeluaran:", rata_rata)
print("NIM:", nim)
print("Status (nim < rata_rata):", bolean)