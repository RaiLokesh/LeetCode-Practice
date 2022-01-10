# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = None
    ptr = None
    check = True
    def iterate(ptr):
        if ptr==None:
            return None
        a = Solution.iterate(ptr.next)
        
        if a:
            if a.val!=ptr.val:
                Solution.check = False
            return a.next
            
        else:
            a = Solution.head
            if a.val != ptr.val:
                Solution.check = False
            return a.next
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Solution.head = head
        Solution.check = True
        Solution.ptr = None
        Solution.iterate(head)
        return Solution.check