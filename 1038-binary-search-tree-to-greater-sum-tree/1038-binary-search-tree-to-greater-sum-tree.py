# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    updated_sum = 0
    def traverse(self, ptr):
        if ptr.right:
            self.traverse(ptr.right)
        ptr.val += Solution.updated_sum
        Solution.updated_sum = ptr.val
        if ptr.left:
            self.traverse(ptr.left)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        Solution.updated_sum = 0
        self.traverse(root)
        return root