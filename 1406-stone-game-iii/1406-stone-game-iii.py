class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            res = float('-inf')
            current_sum = 0
            for k in range(1, 4):
                if i + k - 1 < n:
                    current_sum += stoneValue[i + k - 1]
                    res = max(res, current_sum - dp[(i + k) % 4])
            dp[i % 4] = res

        diff = dp[0]
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna