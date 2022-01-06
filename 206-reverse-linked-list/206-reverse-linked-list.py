# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vali = []
        ptr = head
        i = 0
        while ptr!=None: vali.append(ptr.val); ptr = ptr.next
        ptr = head
        vali = vali[::-1]
        while ptr!=None: ptr.val = vali[i]; i+=1; ptr = ptr.next
        return head