class Solution:
    def countComponents(self, V, edges):
        # Step 1: adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V

        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        components = 0

        # Step 2 & 3
        for i in range(V):
            if not visited[i]:
                components += 1
                dfs(i)

        return components
