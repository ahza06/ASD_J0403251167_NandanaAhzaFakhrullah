#=========================================
#Implementasi Dasar: Node pada Linked List
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#=========================================

#=========================================
#Catatan:
#1. konstruktor selain self, bisa ditambahkan parameter
#2. Class Node merupakan unit dasar dari Linked List 
#3. Traversal adalah proses menelusuri dari head ke none
#4. Proses menghapus dilakukan dengan menggeserkan head
#=========================================

#Membuat class Node 
class Node:
    def __init__(self,data): #konstruktor 
        self.data = data #menyimpan nilai dalam node
        self.next = None #pointer ke node berikutnya

# 1) Meng-asign Node Menggunakan Parameter 
CallNode = Node("A")
CallNode2 = Node("B")
CallNode3 = Node("C")

# 2) Menghubungkan Node Menggunakan Parameter  
CallNode.next = CallNode2
CallNode2.next = CallNode3

# 3) Menentukan Node Pertama
head = CallNode 

# 4) Traversal
current = head 
while current is not None:
    print(current.data)      #menampilkan data pada node saat ini
    current = current.next   #pindah ke node berikutnya 

#==============================================================
#Implementasi Dasar : Linked List + Insert Awal
#==============================================================

class LinkedList: #classs implementasi stack
    def __init__(self):
        self.head = None #awalnya kosong


    def insert_awal(self,data): #push dalam stack
        #1) buat node baru
        NewNode = Node(data) #assign ke parameter 

        #2) node baru menunjuk ke head lama 
        NewNode.next = self.head

        #3) head pindah ke node baru
        self.head=NewNode

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah:", data_terhapus)


    def tampilkan(self):
        current = self.head 
        while current is not None:
            print(current.data)
            current = current.next

print("==========List Baru==========")
ll = LinkedList()
ll.insert_awal("1")
ll.insert_awal("2")
ll.insert_awal("3")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()


