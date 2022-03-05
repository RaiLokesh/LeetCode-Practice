# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint as rd
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = self.calLength(head)
        
    def getRandom(self) -> int:
        m = lambda x, y: rd(x, y)
        ptr = self.head
        for i in range(m(0, self.n-1)):
            ptr = ptr.next
        return ptr.val
    def calLength(self, ptr) -> int:
        n = 0
        while ptr != None:
            n += 1
            ptr = ptr.next
        return n

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()