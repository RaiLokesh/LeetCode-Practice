# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        i = 0
        while ptr!=None:
            i+=1
            ptr = ptr.next
        j = 0
        ptr = head
        while j < i//2:
            j+=1
            ptr = ptr.next
        return ptr