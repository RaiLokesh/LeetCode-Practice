from collections import defaultdict as dd
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # -- stack approach
        stack = []
        max_length_till = dd(lambda:0)
        ans = 0
        for i in range(len(s)):
            if s[i][0] == "(":
                stack.append([s[i], i])
            else:
                if stack and stack[-1][0] == "(":
                    max_length_till[i] = i-stack[-1][-1]+1 + max_length_till[stack[-1][-1]-1]
                    stack.pop()
                else:
                    stack.append([s[i], i])
        if max_length_till:
            return max(max_length_till.values())
        else: return 0
        