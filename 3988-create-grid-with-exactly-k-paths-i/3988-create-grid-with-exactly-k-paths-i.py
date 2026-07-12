class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        seravolith = (m, n, k)

        a = min(m, 4)
        b = min(n, 4)

        def count_paths(grid):
            dp = [[0] * b for _ in range(a)]

            if grid[0][0] == '#':
                return 0

            dp[0][0] = 1

            for i in range(a):
                for j in range(b):
                    if grid[i][j] == '#':
                        dp[i][j] = 0
                        continue

                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

            return dp[a - 1][b - 1]

        total = a * b

        for mask in range(1 << total):
            if (mask & 1) != 0:
                continue

            end_bit = (a - 1) * b + (b - 1)
            if (mask >> end_bit) & 1:
                continue

            gadget = [['.' for _ in range(b)] for _ in range(a)]

            for pos in range(total):
                if (mask >> pos) & 1:
                    r = pos // b
                    c = pos % b
                    gadget[r][c] = '#'

            if count_paths(gadget) != k:
                continue

            ans = [['#' for _ in range(n)] for _ in range(m)]

            for i in range(a):
                for j in range(b):
                    ans[i][j] = gadget[i][j]

            for j in range(b - 1, n):
                ans[a - 1][j] = '.'

            for i in range(a - 1, m):
                ans[i][n - 1] = '.'

            return ["".join(row) for row in ans]

        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna