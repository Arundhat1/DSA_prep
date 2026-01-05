class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        curr  = root
        while curr:
            if not curr.left:
                preorder.append(curr.val)
                curr = curr.right
            else:
				
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
					preorder.append(curr.val)
                    prev.right = curr
                    curr = curr.left
                else:
                    
                    prev.right = None
                    
                    curr = curr.right
        return preorder
