# =================================================
# Nama   : Nandana Ahza Fakhrullah
# NIM    : J0403251167
# Kelas  : B1
# =================================================

# ==========================================================
# Kasus: Optimasi Jaringan Kabel Internet Kampus
# Algoritma: Kruskal
# ==========================================================

# 1. Representasi Weighted Graph (Daftar Edge dari image_4a3331.png)
# Format: (bobot, asal, tujuan)
graph_edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

def solve_kruskal(edges):
    # Mengurutkan semua edge berdasarkan biaya pemasangan terkecil
    edges.sort()
    
    mst = []
    total_cost = 0
    connected_nodes = set()
    
    # List untuk melacak komponen yang terhubung (Simple Disjoint Set logic)
    # Karena graf kecil, kita bisa menggunakan logika keanggotaan set sederhana
    parent = {node: node for edge in edges for node in (edge[1], edge[2])}

    def find(i):
        if parent[i] == i:
            return i
        return find(parent[i])

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        parent[root_i] = root_j

    for cost, u, v in edges:
        # Jika u dan v belum berada dalam komponen yang sama, tidak akan membentuk cycle
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, cost))
            total_cost += cost
            
    return mst, total_cost

# Eksekusi Program
selected_edges, min_total_cost = solve_kruskal(graph_edges)

# 3. Output Edge yang Dipilih
print("--- Jaringan Kabel Optimal (MST) ---")
for u, v, cost in selected_edges:
    print(f"Hubungan: {u} - {v} | Biaya: {cost}")

# 4. Output Total Biaya Minimum
print("-" * 36)
print(f"Total Biaya Minimum = {min_total_cost}")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal.

# 2. Edge mana saja yang dipilih?
#    - GedungC ke GedungD (Biaya 1)
#    - GedungA ke GedungC (Biaya 2)
#    - GedungB ke GedungD (Biaya 3)

# 3. Berapa total biaya minimum?
#    Total biaya minimum adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya adalah menghubungkan seluruh titik (gedung) agar saling 
#    terkoneksi dalam satu jaringan dengan total biaya (bobot edge) yang 
#    paling rendah tanpa adanya jalur redundan (cycle) yang membuang anggaran.