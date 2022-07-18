from collections import defaultdict as dd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        d = dd(lambda:0)
        for i in nums:
            d[i] = 1
        if not head: return 0
        count = 0
        prev = 0
        while head:
            if not d[head.val]:
                if prev: count += 1
                prev = 0
            else:
                prev = 1
            head = head.next
        if prev: count += 1
        return count