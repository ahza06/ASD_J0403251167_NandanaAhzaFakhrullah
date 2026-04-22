#=============================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403251167
#Kelas: TPL B1
#=============================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def search(root, key):
    if root is None:
        print("Data tidak ditemukan.")
        return False
    elif root.data == key:
        return root
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

root = None
data_list = [50, 30, 20, 40, 70, 60, 80]
for data in data_list:
    root = insert(root, data)

print("Data pada Root:", root.data)


print("Data yang sudah terurut:")
inorder_traversal(root)

key = 40
result = search(root, key)
if result:
    print(f"Data {key} ditemukan.")
else:
    print(f"Data {key} tidak ditemukan.")
