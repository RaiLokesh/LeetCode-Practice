from random import randint as rd
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def pick(self, target: int) -> int:
        m = lambda x, y: rd(x, y)
        temp = []
        for i in range(self.n):
            if self.nums[i] == target:
                temp.append(i)
        return temp[m(0, len(temp)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)