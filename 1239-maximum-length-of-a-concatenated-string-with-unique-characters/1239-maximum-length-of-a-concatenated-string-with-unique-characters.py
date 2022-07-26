from collections import defaultdict as dd
class Solution:
    arr = []
    def solve(self, pos, s):
        if pos == len(Solution.arr):
            return len(s)
        
        temp = set()
        for i in range(len(Solution.arr[pos])):
            if Solution.arr[pos][i] not in s:
                temp.add(Solution.arr[pos][i])
            else:
                temp = set()
                break

        s = s.union(temp)
        ans = 0
        for i in range(pos, len(Solution.arr)):
            ans = max(ans, self.solve(i+1, s))
        return ans
    
    def maxLength(self, arr: List[str]) -> int:
        temp = []
        for i in arr:
            if len(i)==len(set(i)):
                temp.append(i)
        arr = temp
        Solution.arr = arr
        visited = set()
        ans = 0
        for i in range(len(arr)):
            ans = max(ans, (self.solve(i, set(arr[i]))))
        return ans