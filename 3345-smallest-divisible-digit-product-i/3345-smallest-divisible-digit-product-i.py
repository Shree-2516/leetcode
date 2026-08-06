class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num):
            prod = 1
            while num > 0:
                prod *= num % 10
                num //= 10
            return prod

        for candidate in range(n, n + 10):
            if get_digit_product(candidate) % t == 0:
                return candidate

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna