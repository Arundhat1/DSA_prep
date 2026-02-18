class Solution:
  def toposort(self,edgeLis,no_nodes):
    stack = []
    graph = [[] for _ in range(no_nodes)]
    for u,v in edgeLis:
      graph[u].append(v)
    visit = [False] * no_nodes
    def dfs(node):
      if visit[node]:
        return
      visit[node] = True
      stack.append(node)
      for nei in graph[node]:
        dfs(nei)
    for i in range(no_nodes):
      if not visit[i]:
        dfs(i)
    order = []
    while stack:
      order.append(stack.pop())
    return order
