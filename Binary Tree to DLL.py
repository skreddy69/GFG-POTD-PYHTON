class Solution:
    def __init__(self):
        # Previous node and head of the doubly linked list
        self.prev = None
        self.head = None
    
    # Helper function to perform in-order traversal and link nodes
    def bToDLLHelper(self, root):
        if root is None:
            return
        
        # Recursively convert the left subtree
        self.bToDLLHelper(root.left)
        
        # Process current node
        if self.prev is None:
            # If this is the first node, set it as the head of DLL
            self.head = root
        else:
            # Link the current node with the previous node
            root.left = self.prev
            self.prev.right = root
        
        # Mark this node as the previous node for the next call
        self.prev = root
        
        # Recursively convert the right subtree
        self.bToDLLHelper(root.right)
    
    # Main function to convert binary tree to doubly linked list
    def bToDLL(self, root):
        self.bToDLLHelper(root)
        return self.head

