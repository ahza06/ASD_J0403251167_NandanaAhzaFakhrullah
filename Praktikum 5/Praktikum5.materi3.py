#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Materi Rekursif: Data List 
#Menggabungkan indeks dari suatu list 
#Mulai dari index 0 hingga index terakhir
#==============================================

def jumlah_list(data, index=0):
    #Base Case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0 #Kembali ke asal apabila list sudah mencapai ujung
    
    #Menambahkan elemen dari index awal hingga index akhir
    return data[index] + jumlah_list(data, index+1)

print(jumlah_list([5,7,10,15])) #output: 37
