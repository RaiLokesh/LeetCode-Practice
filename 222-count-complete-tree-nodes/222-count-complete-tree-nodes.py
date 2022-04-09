# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def count(self, ptr):
        if ptr == None: return
        Solution.ans += 1
        self.count(ptr.left)
        self.count(ptr.right)
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        Solution.ans = 0
        self.count(root)
        return Solution.ans