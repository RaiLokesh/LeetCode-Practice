class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            x = timePoints[i].split(":")
            x = int(x[0])*60 + int(x[1])
            timePoints[i] = x
        timePoints.sort()
        ans = 10**6
        for i in range(1, len(timePoints)):
            ans = min(ans, timePoints[i]-timePoints[i-1])
        ans = min(ans, 1440+timePoints[0] - timePoints[-1])
        return ans