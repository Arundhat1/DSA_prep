#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        node = root
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                root = root.right
            elif not root.right and root.left:
                root = root.left
            elif root.left and root.right:
                curr = root.left
                prev = root
                while curr.right:
                    prev = curr
                    curr = curr.right
                root.val = curr.val
                if prev == root:
                    prev.left = curr.left
                else:
                    prev.right = curr.left
            return root
        while node:
            if node.val < key:
                parent = node
                node = node.right    
            elif node.val > key:
                parent = node
                node = node.left
            elif node.val == key:
                if not node.right and not node.left:
                    if  parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                    break
                elif not node.right and node.left:
                    if parent.left == node:
                        parent.left = node.left
                    elif parent.right == node:
                        parent.right = node.left
                    break
                elif not node.left and node.right:
                    if parent and parent.right and parent.right == node:
                        parent.right = node.right
                    elif parent and parent.left and parent.left == node:
                        parent.left = node.right
                    break
                else:
                    curr = node.left
                    prev = node
                    while curr.right:
                        prev = curr
                        curr = curr.right
                    node.val = curr.val
                    if prev == node:
                        prev.left = curr.left
                    else:
                        prev.right = curr.left

                    break
        return root            
