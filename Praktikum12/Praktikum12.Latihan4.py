# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Set semua jarak ke tak terhingga (infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue untuk melacak node yang akan dieksplorasi (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika kita menemukan jalur yang lebih pendek dari yang ada di queue, abaikan
        if current_distance > distances[current_node]:
            continue
            
        # Pindahkan baris ini ke dalam loop untuk mengeksplorasi tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika jalur baru lebih pendek, update jarak dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Eksekusi fungsi
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    # Perbaikan indentasi
    print(lokasi, "=", jarak, "menit")

'''
Pertanyaan Analisis:
1. Lokasi mana yang paling dekat dari Gerbang?
2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
'''
'''
Jawaban:
1. Kantin
2. 7 menit    
3. Tidak selalu, karena jalur langsung mungkin memiliki bobot yang lebih besar dibandingkan jalur yang melalui beberapa node.
4. Dijkstra cocok karena graph memiliki bobot positif dan kita ingin menemukan jalur terpendek dari satu titik ke titik lainnya.
'''