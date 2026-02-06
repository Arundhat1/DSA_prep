class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = 0
        for value in preorder:
            node = TreeNode(value)
            if not root:
                root = node
            else:
                temp = root
                while temp:
                    if node.val < temp.val:
                        if temp.left:
                            temp= temp.left
                        else:
                            temp.left = node
                            break
                    elif node.val > temp.val:
                        if temp.right:
                            temp = temp.right
                        else:
                            temp.right = node
                            break
        return root 
