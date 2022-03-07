from collections import deque as que
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        q = que([[root, 0]])
        ans = []
        prev, temp = 0, []
        while q:
            x = q.popleft()
            if x[1] > prev:
                if prev%2:
                    ans.append(temp[::-1])
                else:
                    ans.append(temp)
                temp = [x[0].val]
            else:
                temp.append(x[0].val)
            if x[0].left:
                q.append([x[0].left, x[1]+1])
            if x[0].right:
                q.append([x[0].right, x[1]+1])
            prev = x[1]
        if temp:
            if prev%2: ans.append(temp[::-1])
            else: ans.append(temp)
        return ans