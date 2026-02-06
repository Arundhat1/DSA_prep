class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            inorder.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        n = len(inorder)
        i,j = 0,n-1
        while i <j:
            Sum =inorder[i] + inorder[j]
            if Sum  < k:
                i += 1
            elif Sum > k:
                j -= 1
            else:
                return True
        return False
