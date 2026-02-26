def bellman_ford(V,edges):
  dist = [float('inf')] * V
  dist[0] = 0
  for i in range(V-1):
    for u,v,weight in edges:
      if dist[u] != float('inf') and dist[u] + wei < dist[v]:
        dist[v] = dist[u] + wei
  for u,v,weight in edges:
    if dist[u] != float('inf') and dist[u] + weight < dist[v]:
      return -1
  return dist

   
  
