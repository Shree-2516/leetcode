class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)

        dp = {(0, 0): 1}

        for num in nums:
            new_dp = dp.copy()
            for (g1, g2), count in dp.items():

                new_g1 = math.gcd(g1, num) if g1 != 0 else num
                state1 = (new_g1, g2)
                new_dp[state1] = (new_dp.get(state1, 0) + count) % MOD

                new_g2 = math.gcd(g2, num) if g2 != 0 else num
                state2 = (g1, new_g2)
                new_dp[state2] = (new_dp.get(state2, 0) + count) % MOD
            dp = new_dp
        
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna