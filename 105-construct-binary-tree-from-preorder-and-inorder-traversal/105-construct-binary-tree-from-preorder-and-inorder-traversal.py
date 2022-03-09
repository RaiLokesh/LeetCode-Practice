# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solve(preorder, inorder):
            if inorder:
                index = inorder.index(preorder.pop(0))
                ptr = TreeNode(inorder[index])
                ptr.left = solve(preorder, inorder[0:index])
                ptr.right = solve(preorder, inorder[index+1:])
                return ptr
        return solve(preorder, inorder)