# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr2:
            l1, l2 = l2, l1
        ptr1 = l1
        ptr2 = l2
        carry = 0
        while ptr1:
            if ptr2:
                sm = (ptr1.val + ptr2.val + carry)
                ptr1.val = sm % 10
                carry = sm // 10
            else:
                sm = (ptr1.val + carry)
                ptr1.val = sm % 10
                carry = sm // 10
            ptr1 = ptr1.next
            if ptr2: ptr2 = ptr2.next
        
        if carry:
            carry = str(carry)
            ptr1 = l1
            while ptr1.next: ptr1 = ptr1.next
            for i in carry:
                temp = ListNode(int(i))
                ptr1.next = temp
                ptr1 = ptr1.next
                
        return l1