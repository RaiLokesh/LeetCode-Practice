# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    visited_levels = set()
    ans = []
    def view(self, ptr, lvl):
        if lvl not in Solution.visited_levels:
            Solution.visited_levels.add(lvl)
            Solution.ans.append(ptr.val)
        if ptr.right:
            self.view(ptr.right, lvl+1)
        if ptr.left:
            self.view(ptr.left, lvl+1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        Solution.visited_levels = set()
        Solution.ans = []
        self.view(root, 0)
        return Solution.ans