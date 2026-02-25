#=================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh Isi Teks File 
#=================================================

nama_file = "data_mahasiswa.txt"

data_dict = {} #inisialisasi data dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan koma
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }

def baca_data_mahasiswa(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict

buka_data = baca_data_mahasiswa(nama_file)

#==================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Membuat fungsi menampilkan data  
#==================================================

def tampilkan_data(data_dict):
    
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
    #Membuat Header Tabel
    print("\n======= Daftar Mahasiswa =======")
    print(f"{'NIM':10} | {'Nama':<12} | {'Nilai':>5}") #Mengatur Indentasi Pada Setiap Baris
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:10} | {nama:<12} | {nilai:>5}")

#==================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 3: Membuat fungsi mencari data
#==================================================


#Memanggil fungsi menampilkan data 
#ampilkan_data(buka_data)

def cari_data(data_dict):

    nim_cari = input("Masukkan NIM yang dicari: ").strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print(f"========Data Mahasiswa Ditemukan========")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("\n==========Data mahasiswa tidak ditemukan.==========")

#ari_data(buka_data)

#==================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 4: Membuat Fungsi Update Nilai
#==================================================

def update_nilai(data_dict):

    nim_update = input("Masukkan NIM yang akan diupdate nilainya: ").strip()
    if nim_update not in data_dict:
        print("NIM tidak ditemuka, update dibatalkan.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru(0-100): ").strip())
    except ValueError:
        print("Nilai tidak valid, update dibatalkan.")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai di luar rentang, update dibatalkan.")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim_update]["nilai"] = nilai_baru

    print(f"Update Selesai, Nilai {nim_update} berubah dari {nilai_lama} menjadi {nilai_baru}")
                                
#pdate_nilai(buka_data)

#==================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 5:Membuat fungsi langsung simpan data ke file
#==================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in data_dict:
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#impan_data(nama_file, buka_data)
#rint("Data berhasil disimpan ke file.")


#==================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 6: Membuat menu interaktif
#==================================================

def tambah_data(data_dict):
    NIM = input("Masukan NIM:")
    if NIM in data_dict:
        print("Data sudah ada, proses dibatalkan")
    else:
        NAMA = input("Masukan Nama Mahasiswa:" )
        NILAI = int(input("Masukan Nilai Mahasiswa:"))
        data_dict[NIM] = {
            "nama": NAMA,
            "nilai": NILAI
        }
        with open("data_mahasiswa.txt", "a") as file :
            for nim in data_dict:
                nama = data_dict[nim]["nama"]
                nilai = data_dict[nim]["nilai"]
                file.write(f"{nim},{nama},{nilai}\n")

    data_dict.update({NIM: {"nama": NAMA, "nilai": NILAI}})
    print("Data Berhasil Ditambahkan.")


def hapus_data(data_dict):
    nim_update = input("Masukkan NIM yang akan dihapus nilainya: ").strip()
    if nim_update not in data_dict:
        print("NIM tidak ditemuka, update dibatalkan.")
        return
    try:
        print("Data tidak ditemukan, hapus dibatalkan")
    except ValueError:
        print("Nilai tidak valid, update dibatalkan.")
        return
    data_dict.pop(nim_update)
    print("Data berhasil dihapus")
    tampilkan_data(data_dict)

    

#==================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 6: Membuat menu interaktif
#==================================================

def main(): 

    #Menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tampilkan Seluruh Data")
    print("2. Cari data berdasarkan NIM")
    print("3. Update nilai mahasiswa")
    print("4. Simpan data ke file")
    print("5. hapus data mahasiswa")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-5): ").strip()

    if pilihan == "1":
        tampilkan_data(buka_data)
    elif pilihan == "2":    
        cari_data(buka_data)
    elif pilihan == "3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
        print("Data berhasil disimpan ke file.")
    elif pilihan == "5":
        hapus_data(buka_data)
    elif pilihan == "0":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()  #code agar home menu dijalankan lebih awal