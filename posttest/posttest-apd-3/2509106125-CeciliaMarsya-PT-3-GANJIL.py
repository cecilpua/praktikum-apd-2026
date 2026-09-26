# login 
nama_benar = "marsya"
nim_benar = "25"

print("=== LOGIN SYSTEM ===")
username = input("Masukkan username: ")
password = input("Masukkan Password: ")

# nested if 
if username == nama_benar:
    if password == nim_benar:
        print("login berhasil")
        print()
        
        # reward dasar
        reward_dasar = 1000

        print("=== PILIHAN MISI ===")
        print("1. Misi Standar (Bonus 2%)")
        print("2. Misi Sulit (Bonus 5%)")
        print("3. Misi Kritis (Bonus 8%)")
        print("4. Misi Penyelamatan Bumi (Bonus 12%)")
        
        pilihan = input("Pilih nomor misi (1-4): ")

        # percabangan menentukan jenis misi dan bonus
        if pilihan == "1":
            nama_misi = "Misi Standar"
            bonus = reward_dasar * 0.02
        elif pilihan == "2":
            nama_misi = "Misi Sulit"
            bonus = reward_dasar * 0.05
        elif pilihan == "3":
            nama_misi = "Misi Kritis"
            bonus = reward_dasar * 0.08
        elif pilihan == "4":
            nama_misi = "Misi Penyelamatan Bumi"
            bonus = reward_dasar * 0.12
        else:
            nama_misi = ""

        # error handling 
        if nama_misi != "":
            reward_akhir = reward_dasar + bonus

            print()
            print("=== HASIL REWARD ===")
            print("Nama Agent:", username)
            print("Jenis Misi:", nama_misi)
            print("Reward Dasar:", reward_dasar)
            print("Reward Bonus:", bonus)
            print("Total Reward Akhir:", reward_akhir)
        else:
            print("Pilihan misi tidak tersedia!")

    else:
        print("Password salah")
else:
    print("username salah")