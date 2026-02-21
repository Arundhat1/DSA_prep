def shortest_path(source,adj,V):
  stack = []
  visited = [False]*V
  def topo(node):
    visited[node] = True
    for nei,_ in adj[node]:
      if not visited[nei]:
        topo(nei)
    stack.append(node)
  for i in range(V):
    if not visited[i]:
      topo(i)
  distance = [float('inf')] * V
  distance[source] = 0
  while stack:
    node = stack.pop()
    if distance[node] != float('inf'):
      for nei, weight in adj[node]:
        if distance[node] + weight < distance[nei]:
          distance[nei] = distance[node] + weight
    
  return distance
