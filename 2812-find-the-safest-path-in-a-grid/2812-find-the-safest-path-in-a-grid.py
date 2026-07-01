
class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # 1. Multi-source BFS to calculate distance to the nearest thief
        dist = [[float('inf')] * n for _ in range(n)]
        queue = collections.deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        # BFS runs once for the entire grid
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # 2. Dijkstra-like pathfinding using a Max-Heap
        # Priority queue stores (-safeness, r, c)
        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True 

        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            d = -d # Convert back to positive

            # If we reached the destination, return the current bottleneck safeness
            if r == n - 1 and c == n - 1:
                return d

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The safeness of the path is the minimum distance encountered
                    new_safeness = min(d, dist[nr][nc])
                    heapq.heappush(max_heap, (-new_safeness, nr, nc))
                    
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna