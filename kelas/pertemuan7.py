def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
print("Luas persegi:", luas_persegi(7))

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

#Kita panggil fungsinya lalu argumen kita adalah angka 7
print("Luas persegi:", luas_persegi(7))

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas
def total_harga_tanah(panjang, lebar, harga = 100000):
    total = luas_persegi_panjang(panjang, lebar) * harga
    return total

#Kita panggil fungsinya
print("Luas persegi panjang:", luas_persegi_panjang(7, 4))
print("Total harga tanah:", total_harga_tanah(7, 4))


def pengumuman():
    print("Hari ini Pengujian Proyek Akhir")

pengumuman("apd")

nama = "Larry" #global
prodi = "Informatika"
#Membuat variabel lokal
def data():
    nama = "Teknik Kedokteran" #lokal
    prodi = "Kedokteran Lanjut"
print("Nama:", nama)
print("Prodi:", prodi)


def hitung_mundur(n):
    if n == 0:
        print("Selesai")
    else:
        print(n)
        hitung_mundur(n-1)

hitung_mundur(5)


#Variabel global untuk menyimpan data buku
buku = []
#Fungsi untuk menampilkan data buku
def lihat_buku():
    if len(buku) < 0:
        print("Belum ada data buku")
    else:
        print("ID Buku | Judul Buku")
        for indeks in range(len(buku)):
            print(indeks, "|", buku[indeks])

#Fungsi untuk menambah data
def tambah_buku():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
    print("Buku berhasil ditambahkan!")
#Fungsi untuk mengedit data
def edit_buku():
    lihat_buku()
    indeks = int(input("Masukkan ID Buku: "))
    if indeks > len(buku) or indeks < 0:
        print("ID tidak valid")
    else:
        buku_baru = input("Judul baru: ")
if __name__ == " __main__":
    while(True):
      tampilkan_menu()

