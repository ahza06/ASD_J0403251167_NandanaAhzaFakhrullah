#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

# ===============================================================================
# Implementasi DFS
# ===============================================================================

# Representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, node, visited):
    """
    Fungsi untuk melakukan penelusuran graph dengan DFS
    graph   : dictionary yang menyimpan struktur dari graph
    node    : menyimpan node yang sedang dikunjungi
    visited : menyimpan node yang sudah dikunjungi
    """
    # Tandai node yang sedang dikunjungi sebagai sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node yang sedang dikunjungi
    for neighbor in graph[node]:
        # Jika tetangga belum dikunjungi, lakukan rekursi
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()

# --- Menjalankan DFS ---
dfs(graph, "A", visited)