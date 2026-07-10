class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: list[int],
        maxDiff: int,
        queries: list[list[int]]
    ) -> list[int]:

        order = sorted(range(n), key=lambda x: nums[x])

        pos = [0] * n
        values = [0] * n

        for i, idx in enumerate(order):
            pos[idx] = i
            values[i] = nums[idx]

        comp = [0] * n
        cid = 0

        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nxt = [0] * n

        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = n.bit_length()

        jump = [nxt]

        for _ in range(LOG - 1):
            prev = jump[-1]
            cur = [0] * n

            for i in range(n):
                cur[i] = prev[prev[i]]

            jump.append(cur)

        ans = []

        for u, v in queries:

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            if pu == pv:
                ans.append(0)
                continue

            steps = 0
            cur = pu

            for k in range(LOG - 1, -1, -1):
                nxt_pos = jump[k][cur]

                if nxt_pos < pv:
                    cur = nxt_pos
                    steps += (1 << k)

            ans.append(steps + 1)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna