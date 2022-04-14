# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = None
    def traverse(self, ptr, val):
        if ptr == None: return
        if ptr.val == val:
            Solution.ans = ptr
        self.traverse(ptr.left, val)
        self.traverse(ptr.right, val)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        Solution.ans = None
        self.traverse(root, val)
        return Solution.ans