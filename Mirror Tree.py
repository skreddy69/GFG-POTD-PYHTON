class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Base case: If the node is None, return
        if root is None:
            return
        
        # Recursively mirror the left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
