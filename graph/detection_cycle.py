def detect_cycle(V,edges):
   graph = [[] for _ in range(V)]
   for u,v in edges:
      graph[u].append(v)
      graph[v].append(u)
   noc = 0
   components = {}
   visited = [False] * V
   def dfs(node,alis):
      if not visited[node]:
         alst.append(node)
         visited[node] = True
         for i in graph[node]:
            dfs(i,alis)
   for i in range(V):
      if not visited[i]:
         noc += 1
         components[noc] = [i]
         group = components[i]
         dfs(i,group)
   total_cycle = 0
   for i in coponents.keys():
   
      min_edg = len(components[i]) -1
      no_edg = 0
      for j in components[i]:
         for k in graph[j]:
            no_edg += 1
      no_edg = (no_edg) //2
      if no_edg > min_edg:
         total_cycle += 1
   return total_cycle
