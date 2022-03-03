class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack method
        stack = []
        path = path.split('/')
        for i in path:
            if i:
                if i==".":
                    continue
                elif i=="..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
        return "/"+"/".join(stack)