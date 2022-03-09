from collections import defaultdict as dd
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = dd(lambda:[])
        def solve(ptr, i):
            if not ptr: return
            d[~i].append(ptr.val)
            solve(ptr.left, i+1)
            solve(ptr.right, i+1)
        solve(root, 0)
        ans = [[]for i in range(len(d))]
        for i in d:
            ans[i] = d[i]
        return ans