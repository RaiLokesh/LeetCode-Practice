class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = [i for i in nums]
        
        # step 1 : find the pivot point using binary search
        
        i = 0
        j = len(l) -1
        start = 0
        end = len(l) -1 
        if l[0] > l[-1]:
            pp = -1
            while i < j:
                mid = (i+j) // 2
                if l[mid] < l[mid-1]:
                    pp = mid
                    break
                elif l[mid] > l[mid+1]:
                    pp = mid+1
                    break
                elif l[mid] > l[j]:
                    i = mid + 1
                elif l[mid] < l[i]:
                    j = mid - 1
                else:
                    print("Some edge case misses!")
            if target < l[0]:
                start = pp
            else:
                end = pp-1
                
        # step 2 : binary search in the list to find the target
        
        while start <= end:
            mid = (start+end)//2
            if target == l[mid]:
                return mid
            elif target < l[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1