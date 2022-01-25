"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        start = head
        ptr = start
        while ptr!=None:
            x = Node(ptr.val)
            y = ptr.next
            ptr.next = x
            x.next = y
            ptr = x.next
        ptr = start
        i=0
        
        while ptr!=None:
            
            if not i%2:
                print(ptr.val, ptr.next.val)
                if ptr.random!=None:
                    ptr.next.random = ptr.random.next
                else:
                    ptr.next.random=None
            i+=1
            ptr=ptr.next
            
        ptr = start
        i = 0
        if head==None: return None
        start = head.next
        ptr = start
        try:
            while ptr!=None:
                ptr.next = ptr.next.next
                ptr = ptr.next
        except: pass
        return start