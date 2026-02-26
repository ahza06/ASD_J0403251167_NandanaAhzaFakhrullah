#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Materi Rekursif: Faktorial
# 3! = 3 x 2 x 1 base case 0 berhenti 
#==============================================

def faktorial(n):
    if n == 0:
        return 1
    
    else:
        return n*faktorial(n-1)
    
n = input("Masukkan nilai faktorial: ")
print(f'{n}! = {faktorial(int(n))}')