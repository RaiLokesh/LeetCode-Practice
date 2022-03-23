from collections import defaultdict as dd
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    mark_p = dd(lambda:0)
    ans = None
    def traverse(self, ptr, pt):
        if ptr == pt:
            if Solution.mark_p[ptr] and Solution.ans==None: Solution.ans = ptr
            Solution.mark_p[pt] = 1
            return True
        if ptr.left:
            c = self.traverse(ptr.left, pt)
            if c:
                if Solution.mark_p[ptr] and Solution.ans==None: Solution.ans = ptr
                Solution.mark_p[ptr] = 1
                return True
        if ptr.right:
            c = self.traverse(ptr.right, pt)
            if c:
                if Solution.mark_p[ptr] and Solution.ans==None: Solution.ans = ptr
                Solution.mark_p[ptr] = 1
                return True
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        Solution.mark_p = dd(lambda:0)
        Solution.ans = None
        self.traverse(root, p)
        self.traverse(root, q)
        return Solution.ans