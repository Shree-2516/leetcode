class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        for start in range(1, 10):
            num = start
            next_digit = start + 1

            while num <= high and next_digit <= 9:
                num =num * 10 + next_digit
                if low <= num <= high:
                    result.append(num)
                next_digit += 1

        return sorted(result)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna