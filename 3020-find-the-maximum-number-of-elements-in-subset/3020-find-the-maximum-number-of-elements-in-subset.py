from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        counts = Counter(nums)
        ans = 1
        
        if counts[1] > 0:
            c = counts[1]
            if c % 2 == 0:
                c -= 1
            ans = max(ans, c)
            
        sorted_keys = sorted(counts.keys())
        for x in sorted_keys:
            if x == 1: continue
            
            curr = x
            curr_len = 0
            while counts[curr] >= 2:
                curr_len += 2
                curr = curr * curr
            
            if counts[curr] >= 1:
                curr_len += 1
            else:
                curr_len -= 1
                
            ans = max(ans, curr_len)
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna