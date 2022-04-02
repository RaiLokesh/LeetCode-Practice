#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		i = 0
		j = i + 1
		while j < N:
		    if A[j] == A[i]:
		        j += 1
		    else:
		        A[i+1] = A[j]
		        i += 1
		        j += 1
		return i+1

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends