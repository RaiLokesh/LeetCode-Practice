from collections import deque as que
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cardPoints = cardPoints[len(cardPoints)-k:] + cardPoints[:k]
        q = deque([])
        ans = sm = 0
        for i in cardPoints:
            if len(q) == k:
                sm -= q.popleft()
            q.append(i)
            sm += i
            ans = max(ans, sm)
        return ans