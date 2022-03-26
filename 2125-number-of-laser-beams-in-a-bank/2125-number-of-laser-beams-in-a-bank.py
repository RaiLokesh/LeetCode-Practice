class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        count = bank[0].count('1')
        for i in range(1, len(bank)):
            temp = bank[i].count('1')
            if not temp: continue
            ans += count * temp
            count = temp
        return ans