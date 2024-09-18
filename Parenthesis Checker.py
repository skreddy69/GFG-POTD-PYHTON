class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to match closing brackets with opening ones
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        # Traverse the string
        for char in x:
            # If it's an opening bracket, push it onto the stack
            if char in "({[":
                stack.append(char)
            # If it's a closing bracket
            elif char in ")}]":
                # If the stack is empty or the top of the stack doesn't match, return False
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                # Pop the matching opening bracket from the stack
                stack.pop()
        
        # If the stack is empty, return True (balanced), otherwise return False (unbalanced)
        return len(stack) == 0