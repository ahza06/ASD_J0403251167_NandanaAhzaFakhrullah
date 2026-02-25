#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#===============================================
#Implementasi Dasar: Queue Berbasis Linked List
#===============================================

#Membuat class Node 
class Node:
    def __init__(self,data): #konstruktor 
        self.data = data #menyimpan nilai dalam node
        self.next = None #pointer ke node berikutnya

#Queue dengan 2 pointer: front and rear 
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None 

    def enqueue(self, data):
        New_Node = Node(data)
        #Jika queue kosong, front dan rear menunjuk ke node yang sama 
        if self.rear is None:
            self.front = New_Node
            self.rear = New_Node
            return
        #jika queue tidak kosong
        #rear lama menunjuk ke Node baru
        self.rear.next = New_Node
        #rear pindah ke node baru
        self.rear = New_Node

    def dequeue(self):
        #1) pilih data yang paling depan
        data_terhapus = self.front.data
        #2) geser front ke next node 
        self.front = self.front.next
        #3) kondisional apabila front menjadi none, queue menjadi kosong
        if self.front is None:
            self.rear = None
        
        return data_terhapus
    print("data yang ingin dihapus tidak ada")



    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear 
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di Node Terakhir")

QLL = QueueLL()
QLL.enqueue("1")
QLL.enqueue("2")
QLL.enqueue("3")
QLL.enqueue("4")
QLL.tampilkan()
    
QLL.dequeue()
QLL.tampilkan()