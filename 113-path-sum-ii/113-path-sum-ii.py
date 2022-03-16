# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        ans = []
        def function(ptr, l):
            if ptr.left == None and ptr.right == None:
                l += [ptr.val]
                if sum(l) == targetSum:
                    ans.append([i for i in l])
                return
            if ptr.left:
                function(ptr.left, l+[ptr.val])
            if ptr.right:
                function(ptr.right, l+[ptr.val])
        function(root, [])
        return ans