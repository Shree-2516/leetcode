class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        currentSum = 0
        count = 0

        for num in nums:
            currentSum += num

            required = currentSum - k

            if required in hashmap:
                count += hashmap[required]
            hashmap[currentSum] = hashmap.get(currentSum, 0) + 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna