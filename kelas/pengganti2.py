kendaraan = input ("Masukan jenis kendaraan Anda: ")

if kendaraan == "mobil":
    tarif_parkir = 10_000
elif kendaraan == "motor":
    tarif_parkir = 5_000
else:
    tarif_parkir = 15.000

print("Tarif parkir yang harus dibayar:", tarif_parkir)