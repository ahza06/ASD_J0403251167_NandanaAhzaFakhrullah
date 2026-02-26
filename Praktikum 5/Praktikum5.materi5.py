#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Konsep Dasar: Backtracking 2
#Pengambilan keputusan melalui beberapa kemungkinan
#==============================================

#Base case penentuan data yang ingin di input kedalam fungsi
def biner_batas(n, batas, hasil="", jumlah_1=0):
    if jumlah_1 > batas:   #Menentukan batas angka yang ada berdasarkan input
        return             #Kembali ke asal apabila jumlah angka 1 sudah melebihi batas yang ditentukan
         
    if len(hasil) == n:    #Base case: jika panjang string sudah n, cetak hasil
        print(hasil)
        return
    
    biner_batas(n, batas, hasil + "0", jumlah_1)        #
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)