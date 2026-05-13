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
        
#Membuat Fungsi Postorder: :Left ==> Root ==> Right
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

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

print("Hasil Postorder Transversal")
postorder(root)

#Penjelasan:...............................
'''Postorder Traversal adalah salah satu metode untuk mengunjungi semua node dalam sebuah pohon biner. Dalam metode ini, kita mengunjungi subtree kiri terlebih dahulu, kemudian kita mengunjungi subtree kanan, dan terakhir kita mengunjungi node saat pertama kali kita menemukannya (root). Urutan kunjungan adalah Left ==> Right ==> Root.'''