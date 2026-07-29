class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        half = [x // 2 for x in freq]
        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + 97)
                break

        total = sum(half)

        ways = 1
        rem = total
        for c in half:
            if c:
                ways *= comb(rem, c)
                rem -= c

        if ways < k:
            return ""

        left = []

        while total:
            for i in range(26):
                if half[i] == 0:
                    continue
                cnt = ways * half[i] // total
                if k > cnt:
                    k -= cnt
                else:
                    left.append(chr(i + 97))
                    ways = cnt
                    half[i] -= 1
                    total -= 1
                    break

        left = "".join(left)
        return left + mid + left[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna