class Solution:
    def maxLength(self, s: str) -> int:
        # Initialize a stack with -1 to serve as a base for valid substrings
        stack = [-1]
        max_len = 0
        
        # Iterate through the string
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of the opening parenthesis
                stack.append(i)
            else:
                # Pop the last unmatched opening parenthesis
                stack.pop()
                
                if len(stack) == 0:
                    # If stack is empty, push the current index as a new base
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
        
        return max_len