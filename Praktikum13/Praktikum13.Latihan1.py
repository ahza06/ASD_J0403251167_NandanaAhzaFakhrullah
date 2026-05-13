# =================================================
# Nama   : Nandana Ahza Fakhrullah
# NIM    : J0403251167
# Kelas  : B1
# =================================================

# ==========================================================
# Implementasi Basic Mengenai Spanning Tree
# ==========================================================

# Daftar edge graph 
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid (n-1 edges, no cycles)
# Kita hubungkan A-C, C-D, dan D-B untuk mencakup semua node
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# 1. Menampilkan daftar edge pada graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# 2. Menampilkan contoh spanning tree yang valid
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 3. Menampilkan jumlah edge pada graph awal
print("\nJumlah edge graph =", len(edges))

# 4. Menampilkan jumlah edge pada spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal adalah representasi seluruh koneksi yang tersedia dan bisa memiliki 
#    cycle (sirkuit). Spanning tree adalah subset dari graph tersebut yang 
#    menghubungkan semua titik (vertex) tanpa membentuk cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena secara definisi, "tree" (pohon) dalam teori graph adalah graph yang 
#    terhubung dan asiklik (tidak memiliki sirkuit). Jika ada cycle, maka ada 
#    jalur redundan yang tidak diperlukan untuk menghubungkan semua titik.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya menggunakan jumlah minimum edge yang diperlukan 
#    untuk menjaga semua node tetap terhubung. Untuk graph dengan n node, 
#    spanning tree akan selalu memiliki tepat n-1 edge.