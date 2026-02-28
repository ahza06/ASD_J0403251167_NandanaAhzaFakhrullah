#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Studi Kasus: Generator Pin
#==============================================
#Base Case untuk permulaan kasus
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang: #Menentukan apabila list setara dengan length
        print(hasil)
        return
    
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)
