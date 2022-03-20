class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def solve(word1, word2):
            if word1 and word2:
                if word1 == word2:
                    return 0
                if word1[0] != word2[0]:
                    return 1 + min(solve(word1[1:], word2), solve(word1[1:], word2[1:]),                                        solve(word1, word2[1:]))
                else:
                    return solve(word1[1:], word2[1:])
            else:
                if word1 == word2 == "":
                    return 0
                elif word1:
                    return (1 + solve(word1[1:], word2))
                else:
                    return (1+ solve(word1, word2[1:]))
        
        return solve(word1, word2)