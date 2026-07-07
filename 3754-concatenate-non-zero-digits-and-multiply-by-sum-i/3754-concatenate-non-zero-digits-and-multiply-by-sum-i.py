class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        non_zero_digits = [d for d in s if d != '0']
        if not non_zero_digits:
            return 0
        x = int("".join(non_zero_digits))
        digit_sum = sum(int(d) for d in non_zero_digits)
        return x * digit_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna