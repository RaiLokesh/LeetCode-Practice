# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1 = ''
        x2 = ''
        while l1!=None:
            x1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            x2+=str(l2.val)
            l2=l2.next
        x1=x1[::-1]
        x2=x2[::-1]
        y = (int(x1)+int(x2))
        x = ListNode(0)
        if y==0: return x
        start=x
        while y!=0:
            x3=y%10
            a = ListNode(x3)
            x.next=a
            x=a
            y//=10
        return start.next