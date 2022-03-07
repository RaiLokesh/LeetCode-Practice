from collections import defaultdict as dd
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dA = dd(lambda:0)
        dB = dd(lambda:0)
        A = B = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if dB[secret[i]]:
                    B += 1
                    dB[secret[i]] -= 1
                else:
                    dA[secret[i]] += 1
                if dA[guess[i]]:
                    B += 1
                    dA[guess[i]] -= 1
                else:
                    dB[guess[i]] += 1
        return str(A)+"A"+str(B)+"B"