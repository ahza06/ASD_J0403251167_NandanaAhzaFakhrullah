#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latihan3: Tracing Insertion Sort
#==============================================


#Buat program dengan menggunakan algoritma insertion sort
#Tracing dengan data = [5, 2, 4, 6, 1, 3]
#Soal:
#1. Tuliskan isi list setelah iterasi i = 1.
#2. Tuliskan isi list setelah iterasi i = 3.
#3. Berapa kali pergeseran terjadi pada iterasi i = 4?

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]  
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key   
    return data

#[Jawaban]
#1. Setelah iterasi i = 1 -> [2, 5, 4, 6, 1, 3] 
#2. Setelah iterasi i = 3 -> [2, 4, 5, 6, 1, 3]
#3. 4 kali
