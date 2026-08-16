class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        count = [0, 0, 0]
        for s in stones:
            count[s % 3] += 1
        
        c1 = count[1]
        c2 = count[2]
        c0 = count[0]
        
        if c1 == 0 and c2 == 0:
            return False
        
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0
        else:
            return abs(c1 - c2) > 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna