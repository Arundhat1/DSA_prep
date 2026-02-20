from collections import deque

def kahn_topological_sort(n, edges):
    """
    n = number of nodes (0 to n-1)
    edges = list of (u, v) meaning u -> v
    """
    
    # Step 1: Build graph and indegree array
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # Step 2: Add all nodes with indegree 0 to queue
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    topo_order = []
    
    # Step 3: Process queue
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check for cycle
    if len(topo_order) != n:
        return []  # Graph has a cycle
    
    return topo_order
