class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        tree_lchar = [''] * (4 * n)
        tree_rchar = [''] * (4 * n)
        tree_len = [0] * (4 * n)

        def push_up(node):
            left = 2 * node
            right = 2 * node + 1
            
            tree_lchar[node] = tree_lchar[left]
            tree_rchar[node] = tree_rchar[right]
            tree_len[node] = tree_len[left] + tree_len[right]
            
            tree_pref[node] = tree_pref[left]
            if tree_lchar[left] == tree_rchar[left] and tree_pref[left] == tree_len[left] and tree_lchar[left] == tree_lchar[right]:
                tree_pref[node] += tree_pref[right]
                
            tree_suff[node] = tree_suff[right]
            if tree_rchar[right] == tree_lchar[right] and tree_suff[right] == tree_len[right] and tree_rchar[right] == tree_rchar[left]:
                tree_suff[node] += tree_suff[left]
                
            cross = 0
            if tree_rchar[left] == tree_lchar[right]:
                cross = tree_suff[left] + tree_pref[right]
                
            tree_max[node] = max(tree_max[left], tree_max[right], cross)

        def build(node, start, end):
            if start == end:
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_max[node] = 1
                tree_lchar[node] = s[start]
                tree_rchar[node] = s[start]
                tree_len[node] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            push_up(node)

        def update(node, start, end, idx, char):
            if start == end:
                s[idx] = char
                tree_lchar[node] = char
                tree_rchar[node] = char
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            push_up(node)

        build(1, 0, n - 1)
        res = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            res.append(tree_max[1])
            
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna