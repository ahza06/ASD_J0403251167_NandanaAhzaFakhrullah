#=============================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403251167
#Kelas: TPL B1
#=============================
#Class Node digunakan untuk 
class Node:
    def __init__(self, data):
        self.data = data # Simpan Nilai
        self.left = None
        self.right = None

# Membuat root (taruh di LUAR class, indentasi ditarik kembali ke kiri)
root = Node("A") # Membuat Node dengan data "A" dan menyimpannya sebagai root
root.left = Node("B") # Membuat Node dengan data "B" dan menyimpannya sebagai left child dari root
root.right = Node("C") # Membuat Node dengan data "C" dan menyimpannya sebagai right child dari root

# Print hasilnya
print("Data Pada Root:", root.data)
print("Data Pada Left Child:", root.left.data)
print("Data Pada Right Child:", root.right.data)

#Pembahasan: .................................


