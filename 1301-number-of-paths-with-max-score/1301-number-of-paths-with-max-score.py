class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7

        dp_sum = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]

        dp_sum[n-1][n-1] = 0
        dp_count[n-1][n-1] = 1

        for r in range(n -1, -1, -1):
            for c in range(n -1, -1, -1):
                if board[r][c] == 'X' or dp_sum[r][c] == -1:
                    continue

                for dr, dc, in [(-1, 0), (0, -1), (-1, -1)]:
                    nr, nc = r + dr, c +dc
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':

                        val = int(board[nr][nc]) if board[nr][nc] not in ('E','S') else 0
                        new_sum = dp_sum[r][c] + val

                        if new_sum > dp_sum[nr][nc]:
                            dp_sum[nr][nc] = new_sum
                            dp_count[nr][nc] = dp_count[r][c]
                        elif new_sum == dp_sum[nr][nc]:
                            dp_count[nr][nc] = (dp_count[nr][nc] + dp_count[r][c]) % MOD
        result_sum = max(0, dp_sum[0][0])
        result_count = dp_count[0][0] if dp_sum[0][0] != -1 else 0
        return [result_sum, result_count]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna