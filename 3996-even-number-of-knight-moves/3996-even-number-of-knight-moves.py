class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        start_parity = (start[0] + start[1]) % 2
        target_parity = (target[0] + target[1]) % 2

        return start_parity == target_parity

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna