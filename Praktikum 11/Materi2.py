#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

#==========================================================
#Implementasi BFS
#==========================================================

#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque

#representasi graph
graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}

def bfs(graph,start):
    #fungsi untuk melakukan penelusuran graph dengan BFS
    #graph : dictionary yang menyimpan struktur dari graph
    #start : node awal penelusuran

    #Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    # visited tabel yang digunakan untuk menyimpan node yang sudah diproses / sudah dikunjungi
    visited = set()

    # Masukkan node awal ke queue
    queue.append(start)

    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft()

        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited:
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

# menjalankan BFS dari node A
bfs(graph, 'A')