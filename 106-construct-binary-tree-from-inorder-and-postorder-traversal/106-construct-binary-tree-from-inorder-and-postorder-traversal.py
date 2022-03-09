# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = postorder[::-1]
        def solve(inorder, postorder):
            if inorder:
                index = inorder.index(postorder.pop(0))
                ptr = TreeNode(inorder[index])
                ptr.right = solve(inorder[index+1:], postorder)
                ptr.left = solve(inorder[0:index], postorder)
                return ptr
        return solve(inorder, postorder)