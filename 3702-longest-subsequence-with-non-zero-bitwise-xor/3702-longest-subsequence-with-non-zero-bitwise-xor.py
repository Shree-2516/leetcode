from functools import reduce

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        if not any(nums):
            return 0
        total_xor = reduce(lambda x, y: x ^ y, nums, 0)
        if total_xor != 0:
            return len(nums)
        return len(nums) - 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna