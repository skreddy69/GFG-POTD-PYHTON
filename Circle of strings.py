from collections import defaultdict, deque

class Solution:
    def isCircle(self, arr):
        def is_strongly_connected(graph, start_node):
            visited = set()
            queue = deque([start_node])
            
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            
            return len(visited) == len(graph)
        
        # Initialize arrays for in-degrees and out-degrees
        in_degree = [0] * 26
        out_degree = [0] * 26
        graph = defaultdict(list)
        
        for s in arr:
            first = ord(s[0]) - ord('a')
            last = ord(s[-1]) - ord('a')
            out_degree[first] += 1
            in_degree[last] += 1
            graph[first].append(last)
        
        # Check if in-degree and out-degree of every character are the same
        for i in range(26):
            if in_degree[i] != out_degree[i]:
                return 0
        
        # Check if the graph is strongly connected
        start_node = ord(arr[0][0]) - ord('a')
        if not is_strongly_connected(graph, start_node):
            return 0
        
        return 1