class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"

        active = s.count("1")

        runs = []
        i = 0
        n = len(t)

        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1

            runs.append((t[i], j - i))
            i = j

        max_gain = 0

        for k in range(1, len(runs) - 1):
            ch, one_len = runs[k]

            if (
                ch == "1"
                and runs[k - 1][0] == "0"
                and runs[k + 1][0] == "0"
            ):
                gain = runs[k - 1][1] + runs[k + 1][1]
                max_gain = max(max_gain, gain)

        return active + max_gain

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna