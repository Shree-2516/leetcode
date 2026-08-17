from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

       
        left_best = [[float("-inf")] * n for _ in range(n)]

       
        right_best = [[float("-inf")] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

            left_best[i][i] = prefix[i + 1]

            right_best[i][i] = -prefix[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                

                lo = i
                hi = j - 1

                while lo <= hi:
                    mid = (lo + hi) // 2

                    left_sum = prefix[mid + 1] - prefix[i]
                    right_sum = prefix[j + 1] - prefix[mid + 1]

                    if left_sum <= right_sum:
                        lo = mid + 1
                    else:
                        hi = mid - 1

                p = hi

                best = 0

                
                if p >= i:
                    best = max(
                        best,
                        left_best[i][p] - prefix[i]
                    )

                
                if p >= i and \
                   prefix[p + 1] - prefix[i] == \
                   prefix[j + 1] - prefix[p + 1]:

                  
                    start = p + 1

                else:
                   
                    start = p + 2

                if start <= j:
                    best = max(
                        best,
                        prefix[j + 1] + right_best[start][j]
                    )

                dp[i][j] = best

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    prefix[j + 1] + dp[i][j]
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    dp[i][j] - prefix[i]
                )

        return dp[0][n - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna