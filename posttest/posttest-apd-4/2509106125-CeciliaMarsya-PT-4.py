user_benar = "marsya"
nim_benar = "2509106125"

gagal = 0
login = False

while gagal < 3:
    print(f"\n--- LOGIN (Percobaan {gagal + 1}/3) ---")
    username = input("Username (Nama): ").strip().lower()
    password = input("Password (NIM) : ").strip()

    if not username or not password:
        print("Input tidak boleh kosong!")
        continue

    # Pengecekan login & deteksi kesalahan
    if username == user_benar and password == nim_benar:
        print("Login Berhasil!")
        login = True
        break
    elif username != user_benar and password != nim_benar:
        print("Username dan Password salah!")
    elif username != user_benar:
        print("Username salah!")
    else:
        print("Password salah!")

    gagal += 1

if not login:
    print("\nGagal login 3 kali. Program berhenti.")

while login:
    print("\n=== MENU DISTRIBUSI PAKET ===")
    print("1. Paket Reguler (1 porsi)")
    print("2. Paket Anak (1 porsi)")
    print("3. Paket Keluarga (4 porsi)")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ").strip()

    if not pilihan:
        print("Input tidak boleh kosong!")
        continue

    if pilihan not in ["1", "2", "3", "4"]:
        print("Opsi tidak valid!")
        continue

    if pilihan == "4":
        print("Terima kasih, program selesai.")
        break

    if pilihan == "1":
        nama_paket = "Paket Reguler"
        porsi = 1
    elif pilihan == "2":
        nama_paket = "Paket Anak"
        porsi = 1
    elif pilihan == "3":
        nama_paket = "Paket Keluarga"
        porsi = 4

    while True:
        jumlah_input = input(f"Masukkan jumlah {nama_paket}: ").strip()

        if not jumlah_input:
            print("Input tidak boleh kosong!")
            continue

        if not jumlah_input.isdigit():
            print("Input harus berupa angka!")
            continue

        jumlah = int(jumlah_input)
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue
        break

    total_porsi = 0
    for i in range(jumlah):
        total_porsi += porsi

    penerima = total_porsi

    if total_porsi >= 20:
        bonus = "5 paket buah"
    elif total_porsi >= 10:
        bonus = "3 botol susu"
    elif total_porsi >= 5:
        bonus = "1 paket vitamin"
    else:
        bonus = "Tidak mendapat bonus"


    print("\n--- HASIL DISTRIBUSI ---")
    print(f"Jenis paket      : {nama_paket}")
    print(f"Jumlah paket     : {jumlah}")
    print(f"Total porsi      : {total_porsi} porsi")
    print(f"Penerima manfaat : {penerima} orang")
    print(f"Bonus            : {bonus}")