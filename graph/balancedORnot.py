# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return max(height(node.left),height(node.right))+1
        if not root:
            return True
        if root.left:
            lf = height(root.left)
        else:
            lf = 0
        if root.right:
            rh = height(root.right)
        else:
            rh = 0
        if abs(lf-rh) > 1:
            return False
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if not left or not right:
            return False
        return True
