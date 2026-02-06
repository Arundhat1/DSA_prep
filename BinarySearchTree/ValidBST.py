class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node = root
        if not root:
            return True
        order = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            order.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        n = len(order)
        for i,num in enumerate(order):
            if i < n-1 and order[i] >= order[i+1]:
                return False


        return True
