class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        node = root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:  # val > node.val (guaranteed by problem)
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break

        return root
