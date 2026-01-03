class Solution:
    # Function to check if two binary trees are identical
    def isSameTree(self, node1, node2):
        # Case 1: If both nodes are NULL, they are identical
        if node1 is None and node2 is None:
            return True

        # Case 2: If only one of the nodes is NULL, they are not identical
        if node1 is None or node2 is None:
            return False

        # Check if the current nodes have the same data value
        # and recursively check their left and right subtrees
        return (node1.val == node2.val) and \
               self.isSameTree(node1.left, node2.left) and \
               self.isSameTree(node1.right, node2.right)
