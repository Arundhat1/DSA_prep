class Solution:
    def rootToNodePath(self, root: Optional[TreeNode], target: int) -> List[int]:
        path = []

        def dfs(node):
            if not node:
                return False

            path.append(node.val)

            if node.val == target:
                return True

            if dfs(node.left) or dfs(node.right):
                return True

            path.pop()   # backtrack
            return False

        dfs(root)
        return path
