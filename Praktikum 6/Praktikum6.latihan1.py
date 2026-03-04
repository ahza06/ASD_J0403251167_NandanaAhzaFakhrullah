#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latihan1: Memahami Kode Program
#==============================================



def insertion_sort(data):
    for i in range(1, len(data)):
     key = data[i]
     j = i - 1

    while j >= 0 and data[j] > key:
     data[j + 1] = data[j]
    j -= 1

    data[j + 1] = key

    return data


#Soal:
    # 1. Mengapa perulangan dimulai dari indeks 1?
    # 2. Apa fungsi variabel key?
    # 3. Mengapa digunakan while, bukan for?
    # 4. Operasi apa yang terjadi di dalam while?

#Jawaban
    # 1. Kode selalu berasumsi bahwa elemen pada indeks 0 sudah dalam keadaan terurut
    # 2. key disini berfungsi sebagai penyimpanan sementara agar sistem dapat menggeser variable tanpa takut kehilangan nilai elemen yang terkait
    # 3. karena while lebih cocok apabila syarat yang dipenuhi tidak pasti kapan berhentinya
    # 4. Penggeseran elemen ke kanan
