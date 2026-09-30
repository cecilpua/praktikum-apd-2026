#studikes2
saldo = int(input("Masukkan jumlah uang saku awal: Rp"))

print(f"Saldo awal: Rp{saldo}")

while saldo > 0:
    pengeluaran = int(input("Masukkan nominal pengeluaran: Rp"))

    if pengeluaran > saldo:
        print("Saldo tidak mencukupi untuk pengeluaran tersebut. Coba nominal yang lebih kecil.")
        continue

    saldo -= pengeluaran
    print(f"Saldo sekarang: Rp{saldo}")

print("Uang saku sudah habis. Program selesai.")