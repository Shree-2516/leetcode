class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp_id = [0] * n
        current_id = 0

        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            comp_id[i] = current_id
        results = []
        for u, v in queries:
            results.append(comp_id[u] == comp_id[v])
        return results
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna