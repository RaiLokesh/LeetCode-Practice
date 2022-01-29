class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(queries)):
            count = 0
            curr_cir = queries[i]
            for j in range(len(points)):
                d = ((curr_cir[0]-points[j][0])**2+(curr_cir[1]-points[j][1])**2)**0.5
                if d<=curr_cir[-1]:
                    count+=1
            ans.append(count)
        return ans