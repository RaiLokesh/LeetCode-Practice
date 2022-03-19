class Solution:
    dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    def check_greater(self, s1, s2):
        if Solution.dictionary[s1] < Solution.dictionary[s2]:
            return -1
        else:
            return 1
    
    def romanToInt(self, s: str) -> int:
        sm = 0
        for i in range(len(s)-1):
            sm += Solution.dictionary[s[i]]*(self.check_greater(s[i], s[i+1]))
        return sm + Solution.dictionary[s[-1]]