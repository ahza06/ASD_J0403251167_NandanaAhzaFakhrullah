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

def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

#Membuat Tree Struktur

#Membuat Kepala
root = Node("Direktur")

#Membuat Child
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#Membuat Child (2)
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")

print("Data Struktur Karyawan")
preorder(root)

#Penjelasan:...............................
'''Preorder Traversal adalah salah satu metode untuk mengunjungi semua node dalam sebuah pohon biner. Dalam metode ini, kita mengunjungi node saat pertama kali kita menemukannya (root), kemudian kita mengunjungi subtree kiri, dan terakhir kita mengunjungi subtree kanan. Urutan kunjungan adalah Root ==> Left ==> Right.'''