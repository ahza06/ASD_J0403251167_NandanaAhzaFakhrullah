#====================================================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#====================================================================

#====================================================================
#Studi Kasus: Sistem Antrian Layanan Akademik
#Implementasi: Queue =>
#Enqueue: Memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue: Memindahkan pointer head (nambah data baru dari depan)
#Stack ==> Front -> C -> B -> A -> None 
#Front -> .... -> Rear
#====================================================================

#1) Mendefinisikan Node(unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim     = nim  #Menyimpan NIM mahasiswa
        self.nama    = nama  #Menyimpan nama mahasiswa
        self.next    = None  #Pointer ke node berikutnya (awal)

#2) Mendefinisikan queue 
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None 

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, nim, nama):
        New_Node = Node(nim, nama)
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
        if self.is_empty():
            print("Antrian kosong, tidak ada yang bisa dilayani.")
            return None
        #1) pilih data yang paling depan
        data_terlayani = self.front
        #2) geser front ke next node
        self.front = self.front.next
        #3) kondisional apabila front menjadi none, queue menjadi kosong
        if self.front is None:
            self.rear = None
        return data_terlayani
    
    def tampilkan(self):
        print("=========Antrian Layanan Akademik=========")
        current = self.front
        no = 1
        while current is not None:
            print(f"[{no}. {current.nim}, {current.nama}]", end=" ")
            current = current.next
            no += 1
        print()  # New line after displaying all elements

def main():
    q = queueAkademik()
    while True:
        print('====== Sistem Antrian Layanan Akademik ======')
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan =  input("Pilih menu (1-4):").strip()

        if pilihan =="1":
            nim = input('Masukkan NIM Mahasiswa: '). strip()
            nama = input('Masukan Nama Mahasiswa: '). strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil ditambahkan ke antrian")

        elif pilihan =="2":
            mahasiswa_layani = q.dequeue()
            if mahasiswa_layani is not None:
                print(f"Mahasiswa Dilayani: {mahasiswa_layani.nim} - {mahasiswa_layani.nama}")
            
        elif pilihan =="3":
            q.tampilkan()

        elif pilihan =="4":
            print("Program Selesai. Terima kasih!")
            break

        else:
            print('Pilihan Tidak Valid, Silahkan Coba Lagi!')

if __name__ == "__main__":
    main()