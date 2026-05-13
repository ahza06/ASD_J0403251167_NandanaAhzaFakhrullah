import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Key utama adalah kota asal, value-nya adalah dictionary berisi kota tujuan dan bobot (jarak/waktu)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {} # Node tujuan akhir yang tidak memiliki cabang keluar
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node 'start' 
    ke seluruh node lainnya dalam graph menggunakan algoritma Dijkstra.
    """
    # Inisialisasi semua jarak ke nilai tak terhingga (inf)
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan node yang sedang dievaluasi. 
    # Format: (jarak_akumulatif, nama_node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Ambil node dengan jarak terpendek saat ini dari antrean
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika ditemukan jarak dalam antrean yang lebih besar dari jarak yang sudah dicatat,
        # maka kita abaikan (karena sudah menemukan rute yang lebih baik)
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua kota tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Kalkulasi jarak total dari node awal ke kota tetangga melalui node saat ini
            distance = current_distance + weight
            
            # Jika rute baru ini lebih pendek dari rute yang sebelumnya diketahui, lakukan update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Masukkan rute yang lebih baik ini kembali ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# 3. Penentuan node awal
node_awal = 'Bogor'

# Menjalankan fungsi Dijkstra
hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

'''
Pertanyaan Analisis:
1. Node awal yang digunakan apa?
2. Node mana yang memiliki jarak paling kecil dari node awal?
3. Node mana yang memiliki jarak paling besar dari node awal?
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

Jawaban Analisis:
1. Node awal yang digunakan adalah 'Bogor'.
2. Node yang memiliki jarak paling kecil dari 'Bogor' adalah 'Depok' dengan jarak 2.
3. Node yang memiliki jarak paling besar dari 'Bogor' adalah 'Bandung' dengan jarak 7.
4. Algoritma Dijkstra bekerja dengan cara memulai dari node awal ('Bogor') dan mengevaluasi semua node tetangga yang dapat dicapai langsung dari node tersebut.
   Setiap kali sebuah node dievaluasi, algoritma akan menghitung jarak total dari node awal ke node tetangga melalui node saat ini. Jika jarak yang dihitung lebih kecil daripada jarak yang sudah diketahui sebelumnya untuk node tetangga tersebut, maka jarak tersebut diperbarui dan node tetangga dimasukkan kembali ke dalam priority queue untuk dievaluasi lebih lanjut.
'''