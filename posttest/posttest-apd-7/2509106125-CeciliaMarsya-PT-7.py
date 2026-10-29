import os

akun = {
    "admin": "125",
    "guest": "521"
}
akun_tambahan = {}
data_penyewaan = {}

paket_studio = {
    "1": {"nama": "Reguler", "durasi": 2, "harga": 75000},
    "2": {"nama": "Premium", "durasi": 4, "harga": 120000},
    "3": {"nama": "VIP", "durasi": 6, "harga": 200000},
    "4": {"nama": "Midnight", "durasi": 8, "harga": 150000},
    "5": {"nama": "Pelajar", "durasi": 2, "harga": 52500}
}

def tampilkan_paket_studio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DAFTAR PAKET STUDIO MUSIK ===")
    for k, v in paket_studio.items():
        print(f"[{k}] {v['nama']} | Durasi: {v['durasi']} jam | Harga: Rp{v['harga']:,}")
    input("\nTekan Enter untuk kembali...")

def tampilkan_penyewaan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DATA PENYEWAAN STUDIO ===")
    if not data_penyewaan:
        print("Belum ada data penyewaan.")
    else:
        for id_p, info in data_penyewaan.items():
            print(f"ID: {id_p}")
            print(f"Nama: {info['nama']}")
            print(f"Paket: {info['paket']}")
            print(f"Status Pembayaran: {info['status']}")
            print(f"Total Harga: Rp{info['harga']:,}")
            print("-" * 35)
        print(f"Total penyewa terdaftar: {len(data_penyewaan)}")
    input("\nTekan Enter untuk kembali...")

def tambah_penyewaan(id_pelanggan, nama_pelanggan):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TAMBAH DATA PENYEWAAN ===")
    try:
        if id_pelanggan in data_penyewaan:
            raise ValueError("ID penyewa sudah terdaftar di sistem!")
        
        print("\nPilih paket studio:")
        for k, v in paket_studio.items():
            print(f"{k}. {v['nama']} | {v['durasi']} jam - Rp{v['harga']:,}")
            
        pilih_paket = input("Masukkan nomor paket (1-5): ")
        
        if pilih_paket not in paket_studio:
            raise KeyError("Nomor paket studio yang dipilih tidak valid!")
            
    except ValueError as ve:
        print(f"Kesalahan Input (ValueError): {ve}")
        input("\nTekan Enter untuk kembali...")
        return
    except KeyError as ke:
        print(f"Kesalahan Pilihan (KeyError): {ke}")
        paket = "Custom"
        harga = 0
    else:
        paket = paket_studio[pilih_paket]['nama']
        harga = paket_studio[pilih_paket]['harga']
        data_penyewaan[id_pelanggan] = {
            "nama": nama_pelanggan,
            "paket": paket,
            "status": "Belum Bayar",
            "harga": harga
        }
        print("Data penyewaan berhasil ditambahkan!")
    finally:
        print("[Info] Proses penanganan data penyewaan selesai.")
        input("Tekan Enter untuk kembali...")

def ubah_data_penyewaan(id_pelanggan):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== UBAH DATA PENYEWAAN ===")
    if id_pelanggan in data_penyewaan:
        print("1. Ubah Nama")
        print("2. Ubah Paket")
        print("3. Ubah Status Pembayaran")
        try:
            pilihan = input("Pilih data yang ingin diubah (1-3): ")
            if pilihan == "1":
                data_penyewaan[id_pelanggan]['nama'] = input("Masukkan nama baru: ")
            elif pilihan == "2":
                for k, v in paket_studio.items():
                    print(f"{k}. {v['nama']} | {v['durasi']} jam - Rp{v['harga']:,}")
                pilih_paket = input("Masukkan nomor paket baru: ")
                if pilih_paket in paket_studio:
                    data_penyewaan[id_pelanggan]['paket'] = paket_studio[pilih_paket]['nama']
                    data_penyewaan[id_pelanggan]['harga'] = paket_studio[pilih_paket]['harga']
                else:
                    raise ValueError("Pilihan paket tidak tersedia.")
            elif pilihan == "3":
                data_penyewaan[id_pelanggan]['status'] = input("Masukkan status baru (Belum Bayar/Lunas): ")
            else:
                raise ValueError("Pilihan menu ubah tidak valid.")
            print("Data berhasil diubah!")
        except ValueError as err:
            print(f"Error Terdeteksi: {err}")
    else:
        print("Data penyewa tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")

def konfirmasi_keluar():
    keluar = input("Yakin ingin keluar? (y/n): ").lower()
    if keluar == "y":
        print("Terima kasih telah menggunakan sistem studio musik.")
        return True
    elif keluar == "n":
        return False
    else:
        print("Input tidak valid, silakan ulangi.")
        return konfirmasi_keluar()

def main_menu_studio(is_admin):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== MENU UTAMA STUDIO MUSIK ===")
        print("1. Tambah Data Penyewaan")
        print("2. Lihat Data Penyewaan")
        if is_admin:
            print("3. Ubah Data Penyewaan")
            print("4. Hapus Data Penyewaan")
        print("5. Lihat Daftar Paket Studio")
        print("6. Logout")
        
        menu = input("Pilih menu: ")
        if menu == "1":
            id_p = input("Masukkan ID penyewa: ")
            nama = input("Masukkan nama penyewa: ")
            tambah_penyewaan(id_p, nama)
        elif menu == "2":
            tampilkan_penyewaan()
        elif menu == "3" and is_admin:
            id_edit = input("Masukkan ID penyewa yang ingin diubah: ")
            ubah_data_penyewaan(id_edit)
        elif menu == "4" and is_admin:
            id_hapus = input("Masukkan ID penyewa yang ingin dihapus: ")
            if id_hapus in data_penyewaan:
                del data_penyewaan[id_hapus]
                print("Data penyewa berhasil dihapus!")
            else:
                print("Data tidak ditemukan.")
            input("\nTekan Enter untuk kembali...")
        elif menu == "5":
            tampilkan_paket_studio()
        elif menu == "6":
            break
        else:
            print("Menu tidak valid.")
            input("Tekan Enter untuk kembali...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM MANAJEMEN PENYEWAAN STUDIO MUSIK ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")
    pilih_awal = input("Pilih menu: ")
    
    if pilih_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN SISTEM STUDIO MUSIK ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in akun and akun[username] == password:
            print("Login berhasil sebagai admin!" if username == "admin" else "Login berhasil!")
            input("Tekan Enter untuk lanjut...")
            main_menu_studio(username == "admin")
        elif username in akun_tambahan and akun_tambahan[username] == password:
            print("Login berhasil!")
            input("Tekan Enter untuk lanjut...")
            main_menu_studio(False)
        else:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter untuk kembali...")

    elif pilih_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        try:
            new_user = input("Masukkan username baru: ")
            if len(new_user) < 3:
                raise ValueError("Username minimal harus memiliki 3 karakter!")
                
            new_pass = input("Masukkan password baru: ")
            if len(new_pass) < 3:
                raise ValueError("Password minimal harus memiliki 3 karakter!")
                
            if new_user in akun or new_user in akun_tambahan:
                print("Username sudah terdaftar! Silakan coba lagi.")
            else:
                akun_tambahan[new_user] = new_pass
                print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")
        except ValueError as err:
            print(f"Registrasi Gagal: {err}")

        input("Tekan Enter untuk kembali ke menu awal...")

    elif pilih_awal == "3":
        if konfirmasi_keluar():
            break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")