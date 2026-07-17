import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:

        mx = max(nums)

        freq = [0] * (mx + 1)

        for x in nums:
            freq[x] += 1

        count = [0] * (mx + 1)

        for g in range(mx, 0, -1):

            multiples_count = 0

            for multiple in range(g, mx + 1, g):
                multiples_count += freq[multiple]

            pairs = multiples_count * (multiples_count - 1) // 2

            for multiple in range(2 * g, mx + 1, g):
                pairs -= count[multiple]

            count[g] = pairs

        prefix = [0] * (mx + 1)

        for i in range(1, mx + 1):
            prefix[i] = prefix[i - 1] + count[i]

        ans = []

        for q in queries:
            ans.append(bisect.bisect_right(prefix, q))

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna