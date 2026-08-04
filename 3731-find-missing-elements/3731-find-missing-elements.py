class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        return [i for i in range(min_val, max_val + 1) if i not in s]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna