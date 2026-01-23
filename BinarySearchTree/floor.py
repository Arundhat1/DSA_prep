class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the floor of a key
    # in a Binary Search Tree (BST)
    def floorInBST(self, root, key):
        # Initialize the floor variable
        # to store the floor value
        floor = -1
        
        # Traverse the BST until reaching
        # the end or finding the key
        while root:
            # If the key is found, assign it 
            # as the floor value and return
            if root.val == key:
                floor = root.val
                return floor
            
            # If the key is greater than the current
            # node's value, move to the right subtree
            if key > root.val:
                # Update the floor with the current node's
                # value and move to the right subtree
                floor = root.val
                root = root.right
            else:
                # If the key is smaller than the current
                # node's value, move to the left subtree
                root = root.left
        
        # Return the computed floor value
        return floor
