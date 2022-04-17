# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    head = None
    pt = None
    def traverse(self, ptr):
        if ptr.left:
            self.traverse(ptr.left)
            
        if Solution.head:
            Solution.pt.right = TreeNode(ptr.val)
            Solution.pt = Solution.pt.right
            
        if not Solution.head:
            Solution.head = Solution.pt = ptr
            
        if ptr.right:
            self.traverse(ptr.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        Solution.head = None
        Solution.pt = None
        self.traverse(root)
        return Solution.head