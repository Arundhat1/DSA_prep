import heapq
def shortest_path(adj,source,V):
  distance = [float('inf')] * V
  distance[source] = 0
  pq = []
  heapq.heappush(pq, (0, S))
  while pq:
    node,dis = heap.heappop(pq)
    for nei,le in adj(node):
      if le + dis < distance[node]:
        distance[node] = le + dis
        heapq.heappush(pq, (distance[nei], nei))
  return distance  
  
  
  
