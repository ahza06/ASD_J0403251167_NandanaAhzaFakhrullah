#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh Isi Teks File 
#==========================

#membuka file dengan metode read ("r")
with open ("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Hasil Read")
print("Tipe Data", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

print("====membaca file per baris====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris=+1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)

#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : konsep parsing data
#==========================
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai, = baris.split(",") #parsing data berdasarkan koma
        print("NIM :", nim, "Nama :", nama, "Nilai: ", nilai)


data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        data_list.append([nim,nama,int(nilai)])

print("====Data mahasiswa dalam list=====")
print(data_list)

print("====jumlah record dalam list=====")
print("Jumlah record", len(data_list))

print("=====menampilkan data record tertentu====")
print("contoh record pertama", data_list[0])

#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : konsep parsing data
#==========================

data_dict = {} #buat variabel untuk dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        
        data_dict[nim] = {          #Key    #Simpan data mahasiswa ke dictionary dengan key NIM
            "nama": nama,           #values
            "nilai": int(nilai)     #values
        }

print("====Data Mahasiswa dalam Dictionary====")
print(data_dict)