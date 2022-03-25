# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def traverse(self, ptr1, ptr2, target):
        if ptr1 == target:
            Solution.ans = ptr2
            return False
        x = y = True
        if ptr1.left:
            x = self.traverse(ptr1.left, ptr2.left, target)
            if x == False:
                return False
        if ptr1.right:
            y = self.traverse(ptr1.right, ptr2.right, target)
            if y == False:
                return False
        return x and y
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.traverse(original, cloned, target)
        return Solution.ans