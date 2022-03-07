# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    ans = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # -> the inorder traversal of a BST is sorted
        Solution.prev = None
        Solution.ans = True
        def traverse(ptr):
            if ptr.left:
                traverse(ptr.left)
            if Solution.prev != None and Solution.prev >= ptr.val:
                Solution.ans = False
            Solution.prev = ptr.val
            if ptr.right:
                traverse(ptr.right)
        traverse(root)
        return Solution.ans