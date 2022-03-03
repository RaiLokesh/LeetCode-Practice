# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicates = set()
        ptr = head
        while ptr:
            if ptr.next:
                if ptr.val == ptr.next.val:
                    duplicates.add(ptr.val)
            ptr = ptr.next
        
        while head and head.val in duplicates:
            head = head.next
        ptr = head
        while ptr:
            if ptr.next and ptr.next.val in duplicates:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head