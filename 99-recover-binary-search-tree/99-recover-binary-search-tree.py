# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    ans = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        Solution.prev = TreeNode(-1*float('inf'))
        Solution.ans = [None, None]
        def traverse(ptr):
            if ptr == None: return
            
            traverse(ptr.left)
            
            if Solution.ans[0] == None and Solution.prev.val >= ptr.val:
                Solution.ans[0] = Solution.prev
                
            if Solution.ans[0] != None and Solution.prev.val >= ptr.val:
                Solution.ans[1] = ptr
                
            Solution.prev = ptr
            
            traverse(ptr.right)
            
        traverse(root)
        Solution.ans[0].val, Solution.ans[1].val = Solution.ans[1].val, Solution.ans[0].val
        