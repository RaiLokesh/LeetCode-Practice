from collections import deque as que
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        q = [root]
        def function(q):
            if not q: return
            q1 = []
            i = 0
            while i < (len(q)-1):
                q[i].next = q[i+1]
                if q[i].left: q1.append(q[i].left)
                if q[i].right: q1.append(q[i].right)
                i += 1
            q[i].next = None
            if q[i].left: q1.append(q[i].left)
            if q[i].right: q1.append(q[i].right)
            function(q1)
        function(q)
        return root