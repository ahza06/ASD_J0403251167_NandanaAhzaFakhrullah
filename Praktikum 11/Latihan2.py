#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

#=================================================
# Studi Kasus DFS (Pencarian Jalur Terdalam)
#=================================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    # Menandai node saat ini sebagai sudah dikunjungi
    visited.add(node)
    print(node, end=" ")

    # Rekursi ke setiap tetangga yang belum dikunjungi
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Inisialisasi set untuk melacak node yang sudah dikunjungi
visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

'''
Pertanyaan Analisis:
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
Jawab: Karena DFS menggunakan prinsip Stack (LIFO - Last In First Out). 
Dalam implementasi rekursif ini, saat program menemukan tetangga pertama (misal 'B'), 
ia langsung memanggil fungsi dfs() kembali untuk node tersebut sebelum mengecek 
tetangga lainnya ('C'). Hal ini menyebabkan algoritma terus "menyelam" ke cabang 
terdalam sampai menemui node daun (dead end) sebelum melakukan backtracking.

2. Apa yang terjadi jika urutan neighbor diubah?
Jawab: Urutan output penelusurannya akan berubah, meskipun tetap mengikuti pola kedalaman. 
Misalnya, jika 'A': ['C', 'B'], maka DFS akan menyelesaikan jalur A -> C -> F 
terlebih dahulu sebelum mulai mengeksplorasi cabang 'B'.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab:
- Hasil DFS: A B D E C F (Eksplorasi dilakukan per cabang hingga mentok).
- Hasil BFS: A B C D E F (Eksplorasi dilakukan per level/lapisan kedalaman).
DFS lebih cocok untuk mencari solusi di jalur yang dalam atau untuk exhaustive search, 
sedangkan BFS lebih unggul untuk mencari jalur terpendek pada graph tanpa bobot.
'''