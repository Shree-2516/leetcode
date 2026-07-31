class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        sorted_counts = sorted(count.values(), reverse=True)
        
        total_pushes = 0
        for i, freq in enumerate(sorted_counts):
            multiplier = (i // 8) + 1
            total_pushes += freq * multiplier
            
        return total_pushes


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna