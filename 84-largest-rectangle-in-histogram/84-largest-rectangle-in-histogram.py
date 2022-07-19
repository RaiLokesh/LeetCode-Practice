class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [[heights[0], 0]]
        
        left = [-1]*len(heights)
        right = [len(heights)]*len(heights)
        
        for i in range(1, len(heights)):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1][1]
                stack.append([heights[i], i])
            else:
                left[i] = -1
                stack.append([heights[i], i])
        
        stack = [[heights[-1], len(heights)-1]]
        for i in range(len(heights)-2, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1][1]
                stack.append([heights[i], i])
            else:
                right[i] = len(heights)
                stack.append([heights[i], i])
        
        for i in range(len(heights)):
            ans = max(ans, heights[i]*(right[i]-left[i]-1))
        return ans