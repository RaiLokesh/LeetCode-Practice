class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(len(pushed)):
            if pushed[i] != popped[j]:
                stack.append(pushed[i])
            else:
                k = -1
                j += 1
                while len(stack) and j<len(popped) and stack[k] == popped[j]:
                    stack.pop()
                    j+=1
        if not stack: return True
        return False