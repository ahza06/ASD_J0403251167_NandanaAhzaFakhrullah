# =================================================
# Nama   : Nandana Ahza Fakhrullah
# NIM    : J0403251167
# Kelas  : B1
# =================================================

# ==========================================================
# Implementasi Algoritma Prim
# ==========================================================

import heapq

# Representasi Graph 
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    # Menambahkan semua edge dari node awal ke dalam priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        # Mengambil edge dengan bobot terkecil (Greedy)
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Menambahkan edge dari node yang baru dikunjungi ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan fungsi dengan node awal 'A'
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A'.

# 2. Edge mana yang dipilih pertama kali?
#    Edge ('A', 'C') dengan bobot 2, karena merupakan tetangga terdekat 
#    dari node 'A' dengan bobot terkecil.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menentukannya dengan cara melihat semua edge yang menghubungkan 
#    himpunan node yang sudah dikunjungi ke node yang belum dikunjungi, 
#    lalu memilih edge dengan bobot terkecil menggunakan priority queue (heapq).

# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST adalah 6 (terdiri dari edge A-C bobot 2, C-D bobot 1, 
#    dan D-B bobot 3).

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Prim membangun pohon secara bertahap dari satu node awal dan terus 
#    "tumbuh" ke luar. Sedangkan Kruskal fokus pada pengurutan seluruh edge 
#    terkecil di seluruh graph dan menggabungkannya selama tidak membentuk cycle, 
#    meskipun edge tersebut belum terhubung dengan pohon utama (forest).