class Solution:
    # find inorder successor in BST by tracking candidate
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        # initialize successor reference
        successor = None
        # traverse until null
        while root is not None:
            # move left while updating successor when root > p
            if root.val > p.val:
                successor = root
                root = root.left
            # otherwise move right
            else:
                root = root.right
        # return final successor (or None)
        return successor
