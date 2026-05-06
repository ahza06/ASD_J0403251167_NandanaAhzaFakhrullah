#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

#=================================================
# Studi Kasus BFS (Pencarian Jalur Terdekat)
#=================================================


from collections import deque

# Peta jalan atau rute.
# Bagian kiri (Key) itu lokasi saat ini.
# Bagian kanan = tujuan yang bisa didatengin langsung dari lokasi tersebut.
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [], # Kosong berarti jalan buntu, gak ada rute ke tempat lain
    'Pasar': []         # Ini juga jalan buntu
}

def bfs(graph, start):
    # visited ini ibarat buku tamu.
    # Fungsinya buat nyatet tempat mana aja yang udah pernah kita datengin.
    # Ini penting banget biar ga bolak-balik.
    visited = set()
     
    # BFS pakai sistem FIFO (First-In, First-Out), alias siapa yang masuk antrean duluan, 
    # dia yang dieksplorasi/diproses duluan.
    queue = deque([start])

    # Catat lokasi awal (start) ke buku tamu karena kita langsung berdiri di situ
    visited.add(start)

    # Selama antreannya belum kosong, program akan terus jalan nyari rute
    while queue:
        # Panggil lokasi yang ada di antrean paling DEPAN, lalu keluarin dari antrean
        node = queue.popleft()
        
        # Cetak lokasi yang lagi kita kunjungin sekarang di layar
        print(node, end=" ")

        # Sekarang, kita cek semua jalan cabang (tetangga) dari lokasi kita saat ini
        for neighbor in graph[node]:
            # Kalau tempat tetangga itu BELUM ADA di buku tamu (belum pernah dikunjungin)...
            if neighbor not in visited:
                # 1. Catat ke buku tamu biar besok-besok gak didatengin lagi
                visited.add(neighbor)
                
                # 2. Masukin tempat baru itu ke barisan paling BELAKANG di antrean 
                # untuk dikunjungin pada giliran berikutnya
                queue.append(neighbor)

# Eksekusi Program
print("Urutan kunjungan BFS dari Rumah:")
bfs(graph, 'Rumah')
'''
1. Node mana yang dikunjungi pertama?
Node yang dikunjungi pertama adalah 'Rumah'. Secara teknis, dalam algoritma BFS yang diberikan, 
variabel queue diinisialisasi dengan [start], di mana start adalah 'Rumah'. Karena BFS menggunakan 
prinsip FIFO (First-In, First-Out), node awal inilah yang pertama kali di-popleft() dari antrean dan dicetak ke layar.

2. Mengapa BFS cocok untuk mencari jalur terdekat?
BFS sangat efektif untuk mencari jalur terdekat (pada graph tanpa bobot) karena ia melakukan penelusuran secara level-order atau berlapis.
Algoritma ini akan memeriksa semua node di jarak $k$ sebelum pindah ke node di jarak k+1.
Artinya, saat sebuah target ditemukan, kita bisa menjamin bahwa jalur tersebut adalah jalur dengan jumlah edge paling sedikit dari titik awal. 
Tidak ada kemungkinan ada jalur yang lebih pendek di "lapisan" yang lebih dalam.

3.Apa perbedaan urutan BFS jika struktur graph diubah?
Urutan kunjungan BFS sangat bergantung pada topologi (hubungan antar node) dan urutan ketetangga (adjacency list).
Jika kita menambahkan edge langsung dari 'Rumah' ke 'Pasar', maka 'Pasar' akan dikunjungi di level 1 (bersamaan dengan 'Sekolah'), 
bukan lagi setelah 'Toko'.
Jika urutan dalam list diubah (misal: {'Rumah': ['Toko', 'Sekolah']}), maka 'Toko' akan diproses lebih dulu daripada 'Sekolah', 
meskipun keduanya berada di level yang sama. Intinya, setiap perubahan struktur akan mengubah urutan masuknya node ke dalam queue.
'''
