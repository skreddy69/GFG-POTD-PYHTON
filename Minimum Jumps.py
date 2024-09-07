class Solution:
	def minJumps(self, arr):
	    n = len(arr)
        
        # Base case: When the array has only one element
        if n == 1:
            return 0
        
        # If the first element is 0, we can't move forward
        if arr[0] == 0:
            return -1
        
        # Initialization
        maxReach = arr[0]  # The maximum index we can reach
        steps = arr[0]     # The number of steps we can still take
        jumps = 1          # We have to make at least one jump
        
        # Start traversing the array
        for i in range(1, n):
            # Check if we have reached the end of the array
            if i == n - 1:
                return jumps
            
            # Update the maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # We use a step to move forward
            steps -= 1
            
            # If no more steps are left
            if steps == 0:
                # We must have used a jump
                jumps += 1
                
                # Check if the current position is reachable
                if i >= maxReach:
                    return -1
                
                # Re-initialize steps to the number of steps to reach maxReach from position i
                steps = maxReach - i
        
        return -1