class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
    
    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        transformed = [1 if x == target else -1 for x in nums]
        
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + transformed[i]
            
        offset = n + 1
        ft = FenwickTree(2 * n + 1)
        
        count = 0
        ft.update(0 + offset, 1)
        
        for i in range(1, n + 1):
            count += ft.query(prefix_sums[i] + offset - 1)
            ft.update(prefix_sums[i] + offset, 1)
            
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna