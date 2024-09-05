class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_so_far = arr[0]
        current_max = arr[0]

        # Loop through the array from the second element onwards
        for i in range(1, len(arr)):
            # Update the current maximum sum considering the current element
            current_max = max(arr[i], current_max + arr[i])
            
            # Update the overall maximum sum if the current maximum is greater
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far