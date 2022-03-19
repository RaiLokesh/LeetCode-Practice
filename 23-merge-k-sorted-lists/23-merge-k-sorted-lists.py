# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        listss = []
        for i in lists:
            temp = []
            ptr = i
            while ptr:
                temp.append(ptr.val)
                ptr = ptr.next
            listss.append(temp)
            
        for i in range(1, len(listss)):
            listss[0] += listss[i]
        temp = sorted(listss[0])
        if not temp: return None
        ptr = ListNode(temp[0])
        head = ptr
        for i in temp:
            x = ListNode(i)
            ptr.next = x
            ptr = ptr.next
        return head.next