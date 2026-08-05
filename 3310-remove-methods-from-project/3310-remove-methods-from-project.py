class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        from collections import defaultdict, deque

        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)

        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)

        possible = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                possible = False
                break

        if not possible:
            return list(range(n))

        return [i for i in range(n) if i not in suspicious]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna