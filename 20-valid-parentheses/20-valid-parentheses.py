class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ')}]':
                if stack:
                    tc = stack.pop()
                    if (i == ")" and tc != "(") or (i == "}" and tc != "{") or (i == "]" and tc !="["):
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if stack: return False
        return True