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
        
#Fungsi Preorder; Root ==> Left ==> Right
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

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

print("Hasil Preorder Transversal")
preorder(root)

#Penjelasan:...............................
'''
Preorder Traversal adalah salah satu metode untuk mengunjungi semua node dalam sebuah pohon biner. Dalam metode ini, kita mengunjungi node saat pertama kali kita menemukannya (root), kemudian kita mengunjungi subtree kiri, dan terakhir kita mengunjungi subtree kanan. Urutan kunjungan adalah Root ==> Left ==> Right.'''