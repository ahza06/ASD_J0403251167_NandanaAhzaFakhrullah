#=============================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403251167
#Kelas: TPL B1
#=============================
class Node:
    def __init__(self, data):
        self.data = data # Simpan Nilai
        self.left = None
        self.right = None
        
#Membuat Root (Sipaling atas)
root = Node("A")

#Membuat Child level 1 
root.left= Node("B")
root.right = Node("C")
pass

#Membuat Child Level 2 dari B
root.left.left = Node("D")
root.left.right = Node ("E")
pass

#Membuat Child Level 2 dari C
root.right.left = Node("F")
root.right.right = Node ("G")

print("Data Pada Root:", root.data)
print("Data Pada Left Child:", root.left.data)
print("Data Pada Right Child:", root.right.data)
print("Data Pada Left Child dari Left Child:", root.left.left.data)
print("Data Pada Right Child dari Left Child:", root.left.right.data)
print("Data Pada Left Child dari Right Child:", root.right.left.data)
print("Data Pada Right Child dari Right Child:", root.right.right.data)








#Pembahanan:...............................












