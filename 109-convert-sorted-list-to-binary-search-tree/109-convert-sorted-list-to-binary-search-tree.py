# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def make_bst(self, inorder):
        if inorder == []:
            return None
        x = TreeNode(inorder[len(inorder)//2])
        x.left = self.make_bst(inorder[:len(inorder)//2])
        x.right = self.make_bst(inorder[len(inorder)//2+1:])
        return x
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l = []
        ptr = head
        while ptr!=None:
            l.append(ptr.val)
            ptr = ptr.next
        return self.make_bst(l)
        