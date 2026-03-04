#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latihan2: Melengkapi Potongan Kode
#==============================================
_____________ = "Lengkapi"
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and _____________:
        data[j + 1] = data[j]
        j -= 1

    _____________

    return data
# Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending.


#Jawaban Nomer 1
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and  data[j] > key: #Jawaban Nomer 1
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = key #Jawaban Nomer 1

    return data

#Jawaban Nomer 2
def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Tanda "lebih besar" (>) diubah jadi "kurang dari" (<)
        while j >= 0 and data[j] < key: 
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data