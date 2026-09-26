# Nama : marsya
# NIM  : 125 (2 digit terakhir: 25)
# Posttest APD Modul 3 - NIM Genap

# Data login benar
nama_benar = "marsya"
nim_benar = "25"

print("=== LOGIN SYSTEM ===")
username = input("Masukkan username: ")
password = input("Masukkan Password: ")

# Nested if sesuai arahan aslab
if username == nama_benar:
    if password == nim_benar:
        print("login berhasil")
        print()

        # Input total poin
        total_point = float(input("Masukkan total point: "))

        # Error handling jika poin kurang dari 0
        if total_point < 0:
            print("Peringatan: total_point tidak boleh kurang dari 0!")
        else:
            # Penentuan rank dan sisa poin
            if total_point < 100:
                rank = "Rookie"
                sisa_point = 100 - total_point
            elif total_point <= 299:
                rank = "Warrior"
                sisa_point = 300 - total_point
            elif total_point <= 999:
                rank = "Master"
                sisa_point = 1000 - total_point
            elif total_point <= 4999:
                rank = "Grand Master"
                sisa_point = 5000 - total_point
            else:
                rank = "Legend"
                sisa_point = 0

            print()
            print("=== STATUS RANK PLAYER ===")
            print("Username:", username)
            print("Total Point:", total_point)
            print("Rank Saat Ini:", rank)

            # Tampilan penentuan sisa poin
            if rank == "Legend":
                print("Selamat! Anda telah mencapai rank tertinggi!")
            else:
                print("Poin dibutuhkan untuk naik rank:", sisa_point)

    else:
        print("Password salah")
else:
    print("username salah")