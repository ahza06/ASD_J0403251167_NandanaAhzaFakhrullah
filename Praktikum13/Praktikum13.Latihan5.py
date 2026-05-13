# =================================================
# Nama   : Nandana Ahza Fakhrullah
# NIM    : J0403251167
# Kelas  : B1
# =================================================

# ==========================================================
# Implementasi Algoritma Kruskal: Jaringan Jalan Antar Kota
# ==========================================================

# 1. Representasi Weighted Graph
# Format: (bobot, node1, node2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil (Greedy Approach)
edges.sort()

mst = []
total_weight = 0
parent = {}

# Fungsi untuk mencari root dari sebuah node (Path Compression)
def find(i):
    if parent[i] == i:
        return i
    return find(parent[i])

# Fungsi untuk menggabungkan dua set node
def union(i, j):
    root_i = find(i)
    root_j = find(j)
    parent[root_i] = root_j

# Inisialisasi setiap kota sebagai set mandiri
nodes = set()
for _, u, v in edges:
    nodes.add(u)
    nodes.add(v)

for node in nodes:
    parent[node] = node

# Proses pemilihan edge untuk MST
for weight, u, v in edges:
    # Memilih edge jika tidak membentuk cycle
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))
        total_weight += weight

# 3. Output MST
print("--- Minimum Spanning Tree (MST) ---")
for u, v, weight in mst:
    print(f"{u} - {v} (Bobot: {weight})")

# 4. Output Total Bobot Minimum
print("-" * 35)
print(f"Total bobot minimum = {total_weight}")

# 5. Komentar penjelasan program:
# Program menggunakan Algoritma Kruskal untuk mencari jalur penghubung 
# antar kota dengan total biaya/bobot paling efisien. Program mulai dengan 
# mengurutkan semua jalan dari yang termurah, lalu mengambil jalan tersebut 
# selama tidak mengakibatkan jalur berputar (cycle).