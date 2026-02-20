class Solution:
    # Function to perform Topological Sort (Kahn's Algorithm - BFS)
    def topoSort(self, V, adj):
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
          node = q.popleft()
          order.append(node)
          for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
              q.append(nei)
        return order
    def arrange_letters(self,dicto,N,K):
      graph = [[]for _ in range(K)]
      for i in range(N-2):
        mlen = min(len(dicto[i]),len(dicto[i+1]))
        for j in range(mlen):
          if dicto[i][j] != dicto[i+1][j]:
            grpah[ord(dicto[i][j]) -ord('a')].append(ord(doct[i+1][j]) - ord('a'))
      toposort = self.topoSort(K,graph)
      return toposort
            
          
        
