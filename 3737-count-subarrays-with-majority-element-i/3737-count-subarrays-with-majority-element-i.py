class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_valid = 0

        for i in range(n):
            target_count = 0

            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1

                length = j - i + 1

                if target_count * 2 > length :
                    total_valid += 1
        return total_valid
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna