# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt = head
        leng=0
        while pt!=None: pt = pt.next; leng+=1
        if leng<n: return head
        n = leng-n
        print(n)
        if n==0: return head.next
        ptr = head
        for i in range(n-1):
            ptr = ptr.next
        if ptr!=None and ptr.next!=None: ptr.next = (ptr.next).next
        return head