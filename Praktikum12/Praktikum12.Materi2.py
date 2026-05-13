#=========================================
# Nama : Nandana Ahza Fakhrullah
# NIM : J0403251167
# Kelas : TPL B1
#=========================================
# Materi 2 : Implementasi bellman-ford
#=========================================

graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
}

def bellman_ford(graph, start): 
 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
 
        for node in graph: 
 
            for neighbor, weight in graph[node].items(): 
 
                if distances[node] + weight < distances[neighbor]: 
 
                    distances[neighbor] = distances[node] + weight 
 
    return distances

hasil = bellman_ford(graph, 'A') 
print(hasil)