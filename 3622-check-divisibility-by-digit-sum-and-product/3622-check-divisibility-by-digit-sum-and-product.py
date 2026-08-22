class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        temp = n
        
        while temp > 0:
            d = temp % 10
            digit_sum += d
            digit_prod *= d
            temp //= 10
            
        total = digit_sum + digit_prod
        return total != 0 and n % total == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna