# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def solve(self, ptr):
        if ptr == None:
            return 0
        x = y = 0
        if ptr.left:
            x = self.solve(ptr.left.left) + self.solve(ptr.left.right)
        if ptr.right:
            y = self.solve(ptr.right.left) + self.solve(ptr.right.right)
        # curr node level ya uske neeche wale level se hi apana ans milega
        return max(ptr.val + x + y , self.solve(ptr.left) + self.solve(ptr.right))
    
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)