# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxilevel = []
    def dfs(self, ptr, level):
        if level >= Solution.maxilevel[0]:
            if level == Solution.maxilevel[0]:
                Solution.maxilevel[1].append(ptr.val)
            else:
                Solution.maxilevel[0] = level
                Solution.maxilevel[1] = [ptr.val]
        if ptr.left:
            self.dfs(ptr.left, level+1)
        if ptr.right:
            self.dfs(ptr.right, level+1)
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        Solution.maxilevel = [-1, []]
        self.dfs(root, 0)
        return sum(Solution.maxilevel[1])