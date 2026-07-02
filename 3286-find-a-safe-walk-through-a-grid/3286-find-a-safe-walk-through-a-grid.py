import heapq

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        min_obstacles = [[float('inf')] * n for _ in range(m)]
        
        start_cost = grid[0][0]
        min_obstacles[0][0] = start_cost
        
        pq = [(start_cost, 0, 0)]
        
        while pq:
            cost, r, c = heapq.heappop(pq)
            
            if cost > min_obstacles[r][c]:
                continue
            
            if r == m - 1 and c == n - 1:
                return cost < health
                
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]
                    if new_cost < min_obstacles[nr][nc]:
                        min_obstacles[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
                        
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna