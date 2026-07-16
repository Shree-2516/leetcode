import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        current_max = 0

        for x in nums:
            current_max = max(current_max, x)
            prefixGcd.append(math.gcd(x, current_max))

        prefixGcd.sort()

        total_gcd_sum = 0
        left, right = 0, n - 1
        
        while left < right:
            total_gcd_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return total_gcd_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna