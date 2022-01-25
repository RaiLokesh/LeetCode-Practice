# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        if ptr==None: return head
        count = 1
        while ptr.next!=None: ptr = ptr.next; count+=1
        ptr.next = head
        for i in range(count-(k%count)): ptr = ptr.next
        head = ptr.next
        ptr.next = None
        return head
        