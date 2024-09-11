class node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    # Should return data of middle node. If linked list is empty, return -1
    def findMid(self, head):
        # If the linked list is empty, return -1
        if head is None:
            return -1
        
        slow = head
        fast = head
        
        # Move slow by 1 step and fast by 2 steps
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches the end, slow will be at the middle
        return slow.data