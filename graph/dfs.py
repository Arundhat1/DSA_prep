class Solution:
    # Function to perform DFS traversal
    def dfs(self, v, adj, visited, result):
        # Mark current node as visited
        visited[v] = True

        # Store node in result
        result.append(v)

        # Traverse all neighbours
        for u in adj[v]:
            if not visited[u]:
                self.dfs(u, adj, visited, result)
