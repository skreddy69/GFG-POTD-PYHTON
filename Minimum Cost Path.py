import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        # Directions for moving in the grid (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Initialize the dist array with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        
        # Min-heap priority queue
        pq = [(grid[0][0], 0, 0)]  # (cost, x, y)
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            # If we've reached the bottom-right corner
            if x == n - 1 and y == n - 1:
                return cost
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Ensure we stay within bounds
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    
                    # If a cheaper path to (nx, ny) is found
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        # The result will be in the bottom-right corner of the dist array
        return dist[n - 1][n - 1]
