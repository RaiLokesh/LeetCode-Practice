# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preorder = []
    def create_bst(self, inorder):
        if inorder == []:
            return None
        lvl_val = Solution.preorder.pop()
        x = TreeNode(lvl_val)
        x.left = self.create_bst(inorder[:inorder.index(lvl_val)])
        x.right = self.create_bst(inorder[inorder.index(lvl_val)+1:])
        return x
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        Solution.preorder = preorder[::-1]
        return self.create_bst(inorder)