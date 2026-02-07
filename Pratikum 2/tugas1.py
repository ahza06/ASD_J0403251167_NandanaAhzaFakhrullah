
nama_file = "data_barang.txt"

data_dict = {} #inisialisasi data dictionary
with open("data_barang.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
        kode, barang, stok = baris.split(",") #parsing data berdasarkan koma
        data_dict[kode] = {
            "barang": barang,
            "stok": int(stok)
        }


#BACA DATA STOK YANG TERSEDIA
def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, barang, stok = baris.split(",")
            data_dict[kode] = { 
                "barang": barang,
                "stok": int(stok)
            }
    return data_dict

buka_data = baca_data(nama_file)

#TAMPILKAN DATA STOK
def tampilkan_data(data_dict):
    
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
#Membuat Header Tabel
    print("\n======= Daftar Barang =======")
    print(f"{'Kode':10} | {'Nama Barang':<12} | {'Stok':>5}") #Mengatur Indentasi Pada Setiap Baris
    print("-" * 32)

    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["barang"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:10} | {nama:<12} | {stok:>5}")


#PENAMBAHAN/PENGURANGAN LIST BARANG 
def tambah_barang(data_dict):
    print ("\n=== Tambah Barang Baru ===")
    print("1. tambah barang")
    print("2. hapus barang")
    print("0. kembali ke homepage")

    pilihan = input("Pilih menu (0-2): ").strip() #Mengambil input dari user
    if pilihan =="1": 
        KODE = input("Masukan Kode Barang:")
        if KODE in data_dict:
            print("Data sudah ada, proses dibatalkan")
        else:
            NAMA = input("Masukan Nama Barang:" ).strip()
            STOK = int(input("Masukan Stok Barang:").strip())
            data_dict[KODE] = {  #Menyimpan data ke dictionary menggunakan kode sebagai key
                "barang": NAMA,
                "stok": STOK
            }

            with open(nama_file, "w", encoding="utf-8") as file:
                for kode in data_dict:
                    barang = data_dict[kode]["barang"]
                    stok = data_dict[kode]["stok"]
                    file.write(f"{kode},{barang},{stok}\n") #Menulis ulang seluruh data ke file data barang.txt
            print("Data Berhasil Ditambahkan.")

    if pilihan =="2":
        kode_update = input("Masukkan kode [BRGXX] yang akan dihapus nilainya: ").strip()
        if kode_update not in data_dict:
                print("Barang tidak ditemukan, update dibatalkan.")
                return
        else:
            del data_dict[kode_update] #Menghapus data dari dictionary berdasarkan kode yang diinputkan
            with open("data_barang.txt", "w", encoding="utf-8") as file: #Menulis ulang seluruh data ke file data barang
                for kode in data_dict:
                    barang = data_dict[kode]["barang"]
                    stok = data_dict[kode]["stok"]
                    file.write(f"{kode},{barang},{stok}\n")
            tampilkan_data(data_dict)
            
    if pilihan =="0":
        return

 

#UPDATE STOCK
def update_stok(data_dict):

    kode_update = input("Masukkan Kode yang akan diupdate jumlah stoknya: ").strip()
    if kode_update not in data_dict:
        print("Kode tidak ditemukan, update dibatalkan.")
        return
    try:
        stok_baru = int(input("Masukkan jumlah stok baru: ").strip())
    except ValueError:
        print("Nilai tidak valid, update dibatalkan.") #Mengecek apakah input stok baru berupa angka
        return
    if stok_baru < 0: #Kondisional untuk memastikan stok baru tidak negatif
        print("Nilai di luar rentang, update dibatalkan.")

    stok_lama = data_dict[kode]["stok"]
    data_dict[kode_update]["stok"] = stok_baru

    print(f"Update Selesai, Nilai {kode_update} berubah dari {stok_lama} menjadi {stok_baru}")


def main(): #Menjalankan home menu
    buka_data = baca_data(nama_file)


while True:
    print("\n=== HOMEPAGE DATA BARANG ===")
    print("1. Tampilkan Seluruh Barang")
    print("2. Tambah + hapus barang")
    print("3. Update stok barang")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-3): ")

    if pilihan == "1":
        tampilkan_data(buka_data)
    elif pilihan == "2":    
        tambah_barang(buka_data)
    elif pilihan == "3":
        update_stok(buka_data)
    elif pilihan == "0":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()  #code agar home menu dijalankan lebih awal
