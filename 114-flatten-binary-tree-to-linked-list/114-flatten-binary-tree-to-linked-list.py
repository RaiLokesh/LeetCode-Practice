# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(ptr):
            if ptr.left:
                x = solve(ptr.left)
                y = ptr.right
                ptr.right = x
                while x.right:
                    x = x.right
                x.right = y
                ptr.left = None
            if ptr.right:
                solve(ptr.right)
            return ptr
        if not root: return root
        solve(root)