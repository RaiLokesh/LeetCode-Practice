# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    array = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # -> the inorder traversal of a BST is sorted
        Solution.array = []
        def traverse(ptr):
            if ptr.left:
                traverse(ptr.left)
            Solution.array.append(ptr.val)
            if ptr.right:
                traverse(ptr.right)
        traverse(root)
        return Solution.array == sorted(Solution.array) and len(Solution.array) == len(set(Solution.array))