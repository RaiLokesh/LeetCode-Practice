# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        for i in range(a-1):
            ptr = ptr.next
        ptr1 = ptr.next
        for i in range(b-a+1):
            ptr1 = ptr1.next
        ptr.next = list2
        while ptr.next:
            ptr = ptr.next
        ptr.next = ptr1
        return list1