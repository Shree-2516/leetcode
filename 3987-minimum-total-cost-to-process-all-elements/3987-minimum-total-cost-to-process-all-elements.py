class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        sovalemrin = nums  
        MOD = 10**9 + 7
        
        current_resources = k
        total_cost = 0
        ops_done = 0
        
        for num in sovalemrin:
            if current_resources < num:
                needed = num - current_resources
                op_count = (needed + k - 1) // k
                
                start = ops_done + 1
                end = ops_done + op_count
                cost = ((start + end) * op_count) // 2
                
                total_cost = (total_cost + cost) % MOD
                current_resources += op_count * k
                ops_done += op_count
            
            current_resources -= num
            
        return total_cost

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna