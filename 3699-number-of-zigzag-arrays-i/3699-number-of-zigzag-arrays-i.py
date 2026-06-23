class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        dp_up = [1] * k
        dp_down = [1] * k
        
        for _ in range(2, n + 1):
            new_up = [0] * k
            new_down = [0] * k
            
            pref_up = [0] * (k + 1)
            pref_down = [0] * (k + 1)
            for i in range(k):
                pref_up[i+1] = (pref_up[i] + dp_up[i]) % MOD
                pref_down[i+1] = (pref_down[i] + dp_down[i]) % MOD
                
            for v in range(k):
                new_up[v] = pref_down[v]
                
                new_down[v] = (pref_up[k] - pref_up[v+1] + MOD) % MOD
                
            dp_up, dp_down = new_up, new_down
            
        return (sum(dp_up) + sum(dp_down)) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna