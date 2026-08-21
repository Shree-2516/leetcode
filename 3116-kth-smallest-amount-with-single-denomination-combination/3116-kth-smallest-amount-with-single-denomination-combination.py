import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for i in range(1, n + 1):
            for combo in combinations(coins, i):
                l = math.lcm(*combo)
                subsets.append((combo, l))

        def count_amounts(mid):
            total = 0
            for combo, l in subsets:
                if len(combo) % 2 == 1:
                    total += mid // l
                else:
                    total -= mid // l
            return total

        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna