class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for r, s in reservedSeats:
            reserved[r].add(s)
            
        ans = 2 * n
        
        for r, seats in reserved.items():
            left = not any(seat in seats for seat in [2, 3, 4, 5])
            right = not any(seat in seats for seat in [6, 7, 8, 9])
            middle = not any(seat in seats for seat in [4, 5, 6, 7])
            
            if left and right:
                continue
            elif left or right or middle:
                ans -= 1
            else:
                ans -= 2
                
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna