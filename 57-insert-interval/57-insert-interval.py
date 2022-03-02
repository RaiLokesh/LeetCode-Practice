class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        # stack approach
        stack = []
        for i in intervals:
            if stack:
                if i[0] < stack[-1][-1] and i[-1] < stack[-1][-1]:
                    continue
                if i[0] > stack[-1][-1]:
                    stack.append(i)
                else:
                    stack[-1][-1] = i[-1]
            else:
                stack.append(i)
        return stack