class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        size = 2 * k

        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k_idx in range(size):
                    if A[i][k_idx] == 0: continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k_idx] * B[k_idx][j]) % MOD
            return C

        def power(A, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size): res[i][i] = 1
            while p > 0:
                if p % 2 == 1: res = multiply(res, A)
                A = multiply(A, A)
                p //= 2
            return res

        T = [[0] * size for _ in range(size)]
        for v in range(k):
            for u in range(k):
                if u < v: T[u][v + k] = 1 
                if u > v: T[u + k][v] = 1
        
        S2 = [0] * size
        for u in range(k):
            for v in range(k):
                if u < v: S2[v + k] += 1
                elif u > v: S2[v] += 1
        
        if n == 2: return sum(S2) % MOD
        
        Tn_2 = power(T, n - 2)
        res = [0] * size
        for j in range(size):
            for i in range(size):
                res[j] = (res[j] + S2[i] * Tn_2[i][j]) % MOD
                
        return sum(res) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna