class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
            
        s = set(nums)
        ans = prefix_sum
        while ans in s:
            ans += 1
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna