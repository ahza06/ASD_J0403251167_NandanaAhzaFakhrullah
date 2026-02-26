#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latiham 2: Tracing Rekursi
#==============================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)

    countdown(n-1)

    print("Keluar")