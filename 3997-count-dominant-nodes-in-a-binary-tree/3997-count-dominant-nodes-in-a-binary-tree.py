# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        norlavetic = root  
        self.count = 0
        
        def traverse(node):
            if not node:
                return float('-inf')
            
            left_max = traverse(node.left)
            right_max = traverse(node.right)
            
            subtree_max = max(node.val, left_max, right_max)
            
            if node.val >= max(left_max, right_max):
                self.count += 1
            
            return subtree_max
        
        traverse(norlavetic)
        return self.count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna