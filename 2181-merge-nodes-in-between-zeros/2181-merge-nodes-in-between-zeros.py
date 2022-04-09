# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head.next
        new_head = ptr1 = ListNode()
        while ptr.next:
            ptr1.val += ptr.val
            if ptr.val == 0:
                temp = ListNode()
                ptr1.next = temp
                ptr1 = ptr1.next
            ptr = ptr.next
        return new_head