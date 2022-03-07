from collections import deque as que
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # -> not using visited coz no cycles can be present
        if not root: return root
        q = que([[root, 0]])
        ans = []
        prev, temp = 0, []
        while q:
            x = q.popleft()
            if x[1] > prev:
                ans.append(temp)
                temp = [x[0].val]
            else:
                temp.append(x[0].val)
            if x[0].left:
                q.append([x[0].left, x[1]+1])
            if x[0].right:
                q.append([x[0].right, x[1]+1])
            prev = x[1]
        if temp: ans.append(temp)
        return ans