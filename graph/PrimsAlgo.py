import heapq

def PrimAlgo(edges, V):
    adj = [[] for _ in range(V)]
    
    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))
    
    visited = set()
    min_heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    
    while min_heap and len(visited) < V:
        weight, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        total_weight += weight
        
        for nei, w in adj[node]:
            if nei not in visited:
                heapq.heappush(min_heap, (w, nei))
    
    return total_weight
    
