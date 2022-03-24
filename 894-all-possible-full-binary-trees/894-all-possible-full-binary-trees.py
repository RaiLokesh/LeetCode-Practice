# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    @cache
    def solve(self, n):
        if n%2 == 0: return []
        if n == 1: return [TreeNode()]
        curr_root = []
        for left in range(n):
            right = n - left - 1
            left_subTrees = self.solve(left)
            right_subTrees = self.solve(right)
            for i in left_subTrees:
                for j in right_subTrees:
                    curr_root.append(TreeNode(0, i, j))
        return curr_root
                    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.solve(n)