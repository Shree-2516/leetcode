class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
            
        min_score = float('inf')
        visited = set()
        queue = collections.deque([1])
        visited.add(1)
        
        while queue:
            curr = queue.popleft()
            
            for neighbor, dist in adj[curr]:
                min_score = min(min_score, dist)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna