#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Eksekusi fungsi
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    # Perbaikan indentasi pada baris print ini
    print(node, "=", distance)

'''
Pertanyaan Analisis:
1. Berapa bobot langsung dari A ke B?
2. Berapa total bobot jalur A -> C -> B?
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
5. Apa yang dimaksud dengan proses relaksasi edge?
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
'''

'''
Jawaban:
1. 5
2. 2
3. Jalur A -> C -> B
4. Karena Bellman-Ford dapat menangani bobot negatif dan mendeteksi siklus negatif.
5. Proses relaksasi edge adalah proses memperbarui estimasi jarak terpendek ke suatu node jika ditemukan jalur yang lebih pendek.
6. Perbedaan utama Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat menangani bobot negatif dan mendeteksi siklus negatif, sedangkan Dijkstra hanya bekerja dengan bobot positif.
'''