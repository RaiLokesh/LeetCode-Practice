class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        max_height_from_left, max_height_from_right = i, j
        max_area = (j-i) * (min(height[i], height[j]))
        while i<j:
            if height[i] > height[max_height_from_left]:
                #print("hello")
                area = (max_height_from_right - i)*min(height[max_height_from_right], height[i])
                max_area = max(area, max_area)
                
                max_height_from_left = i
            if height[j] > height[max_height_from_right]:
                area = (j - max_height_from_left)*min(height[max_height_from_left], height[j])
                
                max_height_from_right = j
                max_area = max(area, max_area)
            #if max_area == 16: print(i, j)
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return max_area