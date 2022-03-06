# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    duplicate_check = set()
    def copy_bst(ptr, temp):
        if ptr.left:
            x = TreeNode(ptr.left.val)
            temp.left = x
            Solution.copy_bst(ptr.left, temp.left)
        if ptr.right:
            x = TreeNode(ptr.right.val)
            temp.right = x
            Solution.copy_bst(ptr.right, temp.right)
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        Solution.ans = []
        Solution.duplicate_check = set()
        l = [i for i in range(1, n+1)]
        def add(visited, head):
            if len(visited)==len(l):
                # -> copy the bst in temp
                temp = TreeNode(head.val)
                Solution.copy_bst(head, temp)
                # -> if already present in solution, no need to add the bst
                length = len(Solution.duplicate_check)
                Solution.duplicate_check.add(str(temp))
                if length!=len(Solution.duplicate_check):
                    Solution.ans.append(temp)
                return
            for i in l:
                if i not in visited:
                    insertion_point = None
                    ptr = head
                    while ptr:
                        if i < ptr.val:
                            insertion_point = ptr
                            ptr = ptr.left
                        else:
                            insertion_point = ptr
                            ptr = ptr.right
                    if i < insertion_point.val:
                        insertion_point.left = TreeNode(i)
                        add(visited+[i], head)
                        insertion_point.left = None
                    else:
                        insertion_point.right = TreeNode(i)
                        add(visited+[i], head)
                        insertion_point.right = None
        for i in l:
            add([i], TreeNode(i))
        return Solution.ans