class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # partition the string -> check if the left half is a palindrome -> yes: continue in the right half -> no: skip iteration
        def solve(s):
            arr = []
            if not s: return [arr]
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    x = solve(s[i+1:])
                    for j in x:
                        arr.append([s[:i+1]]+j)
            return arr
        return solve(s)
