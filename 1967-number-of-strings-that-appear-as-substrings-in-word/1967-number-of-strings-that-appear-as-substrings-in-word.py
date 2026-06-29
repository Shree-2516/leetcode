class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        
        for p in patterns:
            if p in word:
                count += 1
                
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna