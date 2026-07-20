class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        flat = [val for row in grid for val in row]
        
        shifted = [0] * total
        for i in range(total):
            shifted[(i + k) % total] = flat[i]
            
        res = [[0] * n for _ in range(m)]
        for i in range(total):
            res[i // n][i % n] = shifted[i]
            
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna