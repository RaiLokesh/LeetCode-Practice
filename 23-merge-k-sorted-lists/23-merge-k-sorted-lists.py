import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #if not lists: return None
        def heap_helper(self, other):
            return self.val < other.val
        ListNode.__lt__ = heap_helper # -> used when 2 tasks have same priority
        
        heap = []
        for i in lists:
            if i: heap.append(i)
                
        heapq.heapify(heap)
        
        head = ptr = ListNode()
        
        while heap:
            min_ptr = heapq.heappop(heap)
            node = ListNode(min_ptr.val)
            ptr.next = node
            ptr = ptr.next
            if min_ptr.next:
                heapq.heappush(heap, min_ptr.next)
        
        return head.next