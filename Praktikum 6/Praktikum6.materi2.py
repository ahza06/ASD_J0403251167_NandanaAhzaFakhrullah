#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Insertion Sort (Descending)
#==============================================

def insertion_sort(data):

    #Data Awal
    print("Data Awal: ", data)
    print('='*50)

    #Loop
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        print("Iterasi Ke-", i)
        print("Nilai Asal:", key)
        print("Nilai Terurut: ", data[:i])
        print("Nilai Belum Terurut:", data[i:])

       #Geser
        while j >= 0 and key < data[j]: #
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah Disisipkan:", data)
        print("="*50)
    return data

angka = [7, 8, 5, 2, 4, 6]
print("Hasil Sorting: ", insertion_sort(angka))