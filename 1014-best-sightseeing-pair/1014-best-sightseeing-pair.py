class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        iSm = values[0]
        ans = 0
        for i in range(1, len(values)):
            ans = max(ans, values[i]-i + iSm)
            iSm = max(iSm, values[i]+i)
        return ans