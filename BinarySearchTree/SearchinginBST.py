class Solution:
    # Function to search target in BST
    def searchBST(self, root, target):

        # Loop until current node is null or matches target
        while root and root.val != target:

            # If target is smaller, go to left subtree
            if target < root.val:
                root = root.left

            # If target is larger, go to right subtree
            else:
                root = root.right

        # Return the node if found or None if not
        return root
