import heapq

class Solution:
    def minCost(self, arr):
        # Initialize a min heap
        heapq.heapify(arr)
        
        total_cost = 0
        
        # Keep combining ropes until only one rope is left
        while len(arr) > 1:
            # Pop two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Cost to connect the two ropes
            cost = first + second
            total_cost += cost
            
            # Push the combined rope back into the heap
            heapq.heappush(arr, cost)
        
        return total_cost