#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latiham 1: Rekursi Pangkat
#==============================================

def pangkat(a, n):
    #Base case karena semua angka apabila pangkat 0 hasilnya 1
    if n == 0:
        return 1  #Output dari a^0
    else:
        return a*pangkat(a, n-1) #n-1 disini berfungsi agar looping berhenti sesuai dengan angka pangkat yang di input
    
print(pangkat(5,3)) #output: 125
