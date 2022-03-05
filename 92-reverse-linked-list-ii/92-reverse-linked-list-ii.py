# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr = head
        l = []
        while ptr!=None:
            l.append(ptr.val)
            ptr = ptr.next
        l = l[:left-1] + l[left-1:right][::-1] + l[right:]
        ptr = head
        i = 0
        while ptr!=None:
            ptr.val = l[i]
            ptr = ptr.next
            i += 1
        return head