class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # -> case when one of the lists is empty
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0: return
        
        i = m - 1 # marks the largest element in nums1
        j = n - 1 # marks the largest element in nums2
        pos = m + n - 1 # marks the last available position to add values
        
        while pos >= 0:
            #print(pos, i, j)
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
                pos -= 1
            
            elif j >= 0:
                nums1[pos] = nums2[j]
                j -= 1
                pos -= 1
            
            else:
                break