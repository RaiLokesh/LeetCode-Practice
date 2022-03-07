# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    array = []
    ans = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # -> the inorder traversal of a BST is sorted
        Solution.array = []
        Solution.ans = True
        def traverse(ptr):
            if ptr.left:
                traverse(ptr.left)
            if Solution.array and Solution.array[-1] >= ptr.val:
                Solution.ans = False
            Solution.array.append(ptr.val)
            if ptr.right:
                traverse(ptr.right)
        traverse(root)
        return Solution.ans