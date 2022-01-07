# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict as dd
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = n2 = 0
        ptr1, ptr2 = headA, headB
        while ptr1 or ptr2:
            if ptr1:
                n1+=1
                ptr1 = ptr1.next
            if ptr2:
                n2+=1
                ptr2 = ptr2.next
        if n1>=n2:
            i = 0
            while i<n1-n2:
                headA = headA.next
                i+=1
        else:
            i = 0
            while i<n2-n1:
                headB = headB.next
                i+=1
        while headA and headB:
            if headA==headB: return headA
            headA = headA.next
            headB = headB.next