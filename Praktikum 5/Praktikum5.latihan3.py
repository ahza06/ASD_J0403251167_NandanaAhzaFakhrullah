#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latiham 3: Mencari Nilai Maksimum
#==============================================

def cari_maks(data, index=0):

    if index == len(data) -1:
        return data[index]
    
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))
