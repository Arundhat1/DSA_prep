from collections import deque

def shortest_path(adj, source, V):
    distance = [float('inf')] * V
    q = deque([source])
    
    distance[source] = 0
    
    while q:
        node = q.popleft()
        
        for nei in adj[node]:
            if distance[nei] == float('inf'):  # not visited
                distance[nei] = distance[node] + 1
                q.append(nei)
    
    return distance
