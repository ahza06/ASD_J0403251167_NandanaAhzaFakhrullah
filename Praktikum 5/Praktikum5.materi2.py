#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Materi Rekursif: Call Stack
#Tracing Bilangan  (masuk-keluar)
#input: 3 
#masuk: 1 -> 2 -> 3 
#keluar
#==============================================

def hitung(n):
    #Base case = Kondisi utama dimana fungsi harus berhenti
    if n==0:
        print("selesai")
        return
    
    print("Masuk:", n)   #fase stacking = memanggil fungsi berulang kali hingga menyentuh base case
    hitung(n-1)          #pemanggila rekursif = memanggil fungsi ketika sudah menyentuh syarat yang selanjutnya
    print("keluar", n)   #fase unwinding = kembali ke fungsi sebelumnya 

print("========Program Tracing=========")
n = input("Masukkan nilai: ")
hitung(int(n))