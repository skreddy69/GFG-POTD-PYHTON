class Solution:
    def findNth(self, n: int) -> int:
        # Convert n to base 9 and return as decimal
        result = 0
        base = 1
        
        while n > 0:
            # Get the last digit in base 9
            last_digit = n % 9
            
            # Add to result (treating base 9 number as base 10)
            result += last_digit * base
            
            # Update n and base for the next digit
            n //= 9
            base *= 10
        
        return result
