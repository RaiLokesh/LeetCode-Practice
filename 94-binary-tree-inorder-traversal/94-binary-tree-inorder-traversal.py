# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, ptr, l):
        if ptr.left: self.solve(ptr.left, l)
        l.append(ptr.val)
        if ptr.right: self.solve(ptr.right, l)
        return l
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.solve(root, [])