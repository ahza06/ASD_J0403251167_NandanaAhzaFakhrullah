#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latiham 4: Kombinasi Huruf
#==============================================

def kombinasi(n, hasil=" "):
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)