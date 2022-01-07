# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict as dd
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = dd(lambda:None)
        if not head: return None
        while head.next:
            if d[head]: return True
            d[head] = head
            head = head.next
        return False