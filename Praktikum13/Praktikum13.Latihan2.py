# =================================================
# Nama   : Nandana Ahza Fakhrullah
# NIM    : J0403251167
# Kelas  : B1
# =================================================

# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    # Menggunakan logika: jika salah satu node belum masuk ke set connected
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# --- Pertanyaan Analisis ---

# 1. Edge mana yang dipilih pertama kali?
# Jawab: Edge ('C', 'D') dengan bobot 1.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Jawab: Karena Algoritma Kruskal adalah algoritma "greedy" yang bertujuan mencari 
# total bobot minimum. Dengan mengambil bobot terkecil terlebih dahulu, kita 
# memastikan pohon yang terbentuk memiliki biaya (cost) seefisien mungkin.

# 3. Berapa total bobot MST yang dihasilkan?
# Jawab: Total bobot adalah 6 (hasil dari 1 + 2 + 3).

# 4. Mengapa edge tertentu tidak dipilih?
# Jawab: Edge seperti ('A', 'B') dengan bobot 4 dan ('A', 'D') dengan bobot 5 
# tidak dipilih karena kedua titik ujungnya (A, B dan A, D) sudah terhubung 
# ke dalam struktur MST melalui edge yang lebih murah. Jika dipilih, 
# edge tersebut akan membentuk cycle (sirkuit).