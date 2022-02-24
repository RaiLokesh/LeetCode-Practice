#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visited = [0] * V
        queue = [0]
        visited[0] = 1
        start = 0
        bfs = []
        while start < len(queue):
            bfs.append(queue[start])
            for i in adj[queue[start]]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
            start = start + 1
        return bfs

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends