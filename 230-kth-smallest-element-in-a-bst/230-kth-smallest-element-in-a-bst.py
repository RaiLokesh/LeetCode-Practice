# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    l = []
    def inorder(self, ptr):
        if ptr.left:
            self.inorder(ptr.left)
        Solution.l.append(ptr.val)
        if ptr.right:
            self.inorder(ptr.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        Solution.l = []
        self.inorder(root)
        return Solution.l[k-1]