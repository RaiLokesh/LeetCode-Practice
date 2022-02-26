# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        ptr1 = head
        ptr2 = head.next
        start = ptr2
        prev = None
        while ptr1 and ptr2:
            k = ptr2.next
            ptr2.next = ptr1
            ptr1.next = k
            if prev: prev.next = ptr2
            prev = ptr1
            ptr1 = ptr1.next
            if ptr1: ptr2 = ptr1.next
            
        return start