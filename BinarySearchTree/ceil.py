class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the ceiling of
    # a key in a Binary Search Tree (BST)
    def findCeil(self, root, key):
        # Initialize the variable
        # to store the ceiling value
        ceil = -1
        
        # Traverse the BST until reaching
        # the end or finding the key
        while root:
            # If the key is found, assign it
            # as the ceiling and return
            if root.val == key:
                ceil = root.val
                return ceil
            
            # If the key is greater,
            # move to the right subtree
            if key > root.val:
                root = root.right
            else:
                # If the key is smaller, update ceil
                # and move to the left subtree
                ceil = root.val
                root = root.left
        
        # Return the computed ceiling value
        return ceil
