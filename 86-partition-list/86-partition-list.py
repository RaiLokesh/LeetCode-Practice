# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = left_list = None
        head2 = right_list = None
        while head:
            if head.val < x:
                y = ListNode(head.val)
                if not head1:
                    head1 = left_list = y
                else:
                    left_list.next = y
                    left_list = left_list.next
            else:
                y = ListNode(head.val)
                if not head2:
                    head2 = right_list = y
                else:
                    right_list.next = y
                    right_list = right_list.next
            head = head.next
        if left_list:
            left_list.next = head2
            return head1
        else:
            return head2