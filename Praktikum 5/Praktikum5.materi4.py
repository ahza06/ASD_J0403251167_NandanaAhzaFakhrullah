#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Konsep Dasar: Backtracking
#Pengambilan keputusan melalui beberapa kemungkinan
#==============================================

def biner(n, hasil=""):
    #Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n :
        print(hasil)
        return
    #Stepping stone bagi program untuk tetap menjalankan fungsi
    biner(n,hasil + "0")
    #Stepping stone kedua agar program tetap menjalankan fungsi apabila terdapat suatu obstacle
    biner(n, hasil + "1")
