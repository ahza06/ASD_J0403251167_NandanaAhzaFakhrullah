#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

#=================================================
# Studi Kasus BFS (Pencarian Jalur Terdekat)
#=================================================


from collections import deque

# Representasi graph menggunakan Adjacency List (Dictionary)
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    # 'visited' untuk mencatat node yang sudah diproses agar tidak looping
    visited = set()
    # 'queue' menggunakan prinsip FIFO (First-In, First-Out)
    queue = deque([start])

    visited.add(start)

    while queue:
        # Mengambil elemen pertama dari antrean
        node = queue.popleft()
        print(node, end=" ")

        # Iterasi setiap tetangga dari node saat ini
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Eksekusi Program
print("BFS dari Rumah:")
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
