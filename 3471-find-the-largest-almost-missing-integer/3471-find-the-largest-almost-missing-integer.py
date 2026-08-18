class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        from collections import defaultdict

        counts = defaultdict(set)
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            for x in set(sub):
                counts[x].add(i)

        ans = -1
        for x, sub_indices in counts.items():
            if len(sub_indices) == 1:
                if x > ans:
                    ans = x

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna