class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        node = root
        if not root:
            return 
        def dfs(node):
            if node.left:
                dfs(node.left)
            order.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return order[k-1]
