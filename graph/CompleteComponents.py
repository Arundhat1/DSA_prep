class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete = 0

        # Step 2: traverse components
        for i in range(n):
            if not visited[i]:
                nodes, edge_count = self.dfs(i, graph, visited)

                # Step 3: completeness check
                if edge_count == nodes * (nodes - 1) // 2:
                    complete += 1

        return complete

    def dfs(self, start, graph, visited):
        stack = [start]
        nodes = 0
        edge_count = 0

        while stack:
            node = stack.pop()
            if visited[node]:
                continue

            visited[node] = True
            nodes += 1
            edge_count += len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    stack.append(nei)

        return nodes, edge_count // 2
