# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict as dd
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = dd(lambda:-1)
        ptr = head
        i = 0
        while ptr!=None:
            if d[ptr]!=-1:
                #print(ptr.val)
                return ptr
            #print(ptr.val)
            d[ptr] =i
            i+=1
            ptr = ptr.next
            #print(dict(d))
        return None