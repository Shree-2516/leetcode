class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        unique_vals = set()
        seen_pairs = set()

        for i in range(n):
            for j in range(i, n):
                seen_pairs.add(nums[i] ^ nums[j])

        for p in seen_pairs:
            for x in nums:
                unique_vals.add(p ^ x)

        return len(unique_vals)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna