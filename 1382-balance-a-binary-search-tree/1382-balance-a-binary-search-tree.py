# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sorted_tree = []
    def add_val(self, ptr):
        if ptr.left: self.add_val(ptr.left)
        Solution.sorted_tree.append(ptr.val)
        if ptr.right: self.add_val(ptr.right)
            
    def make_it_balanced(self, array):
        if array == []:
            return None
        x = TreeNode(array[len(array)//2])
        x.right = self.make_it_balanced(array[len(array)//2+1:])
        x.left = self.make_it_balanced(array[:len(array)//2])
        return x
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        Solution.sorted_tree = []
        self.add_val(root)
        return self.make_it_balanced(Solution.sorted_tree)