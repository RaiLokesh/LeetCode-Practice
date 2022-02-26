# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        ptr = head
        val = 0
        while ptr:
            if l==k-1:
                val = ptr
            l+=1
            ptr = ptr.next
        ptr = head
        start = 1
        while start <= l and ptr:
            if start == (l-k)+1:
                ptr.val, val.val = val.val, ptr.val
                return head
            ptr = ptr.next
            start += 1