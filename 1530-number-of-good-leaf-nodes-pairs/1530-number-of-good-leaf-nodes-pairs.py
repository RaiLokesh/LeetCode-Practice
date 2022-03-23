# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        Solution.ans = 0
        def dfs(ptr):
            if not ptr.left and not ptr.right:
                #print(ptr.val)
                return [[0, str(ptr)]]
            leftie = rightie = []
            if ptr.left:
                leftie = dfs(ptr.left)
                for i in leftie:
                    i[0] += 1
            if ptr.right:
                rightie = dfs(ptr.right)
                for i in rightie:
                    i[0] += 1
            combined = leftie + rightie
            for i in leftie:
                for j in rightie:
                    if i[0] + j[0] <= distance:
                        Solution.ans += 1
            #print(ptr.val, combined)
            #if leftie and rightie: print(visited)
            return leftie+rightie
        dfs(root)
        #print(visited)
        return Solution.ans