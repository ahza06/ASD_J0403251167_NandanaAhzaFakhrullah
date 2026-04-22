#==========================================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403251167
#Kelas: TPL B1
#==========================================================

# =========================================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# =========================================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data       # nilai pada node
        self.left = None       # child kiri
        self.right = None      # child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)

    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
        
    return root

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("    " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -------------------------
# Program utama
# -------------------------
root = None

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)


#Pembahasan:
'''Secara keseluruhan, kode ini mendemonstrasikan bahwa urutan input sangat mempengaruhi efisiensi BST. 
Memasukkan data yang sudah terurut (10, 20, 30) membuat pencarian di masa depan menjadi kurang efisien 
dibandingkan jika datanya acak (misal 20, 10, 30), karena pohon menjadi "berat sebelah".'''