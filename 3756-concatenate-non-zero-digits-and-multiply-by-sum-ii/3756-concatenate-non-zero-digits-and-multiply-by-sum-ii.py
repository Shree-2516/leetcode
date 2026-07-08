import bisect

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        
        nz_digits = []
        nz_indices = []
        for i, char in enumerate(s):
            if char != '0':
                nz_digits.append(int(char))
                nz_indices.append(i)
        
        m = len(nz_digits)
        if m == 0:
            return [0] * len(queries)
            
        pref_sum = [0] * (m + 1)
        pref_val = [0] * (m + 1)
        pow10 = [1] * (m + 1)
        for i in range(m):
            pow10[i+1] = (pow10[i] * 10) % MOD
            pref_sum[i+1] = (pref_sum[i] + nz_digits[i]) % MOD
            val = (nz_digits[i] * pow(10, m - 1 - i, MOD)) % MOD
            pref_val[i+1] = (pref_val[i] + val) % MOD
            
        ans = []
        for li, ri in queries:
            start = bisect.bisect_left(nz_indices, li)
            end = bisect.bisect_right(nz_indices, ri) - 1
            
            if start > end:
                ans.append(0)
                continue
            
            digit_sum = (pref_sum[end + 1] - pref_sum[start]) % MOD
            
            range_val = (pref_val[end + 1] - pref_val[start]) % MOD
            inv_pow = pow(pow10[m - 1 - end], MOD - 2, MOD)
            x = (range_val * inv_pow) % MOD
            
            ans.append((x * digit_sum) % MOD)
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna