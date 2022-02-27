class Solution:
    ans = 0
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # binary search on answer
        Solution.ans = 0
        def calculate_trip(t):
            
            trip_done_in_given_time_t = 0
            for i in time:
                trip_done_in_given_time_t += t // i
            if trip_done_in_given_time_t < totalTrips:
                return -1
            else:
                Solution.ans = t
                return 1
        
        start = 0
        end = (max(time) * totalTrips)+1
        while start <= end:
            mid = (start+end) // 2
            temp = calculate_trip(mid)
            if temp == -1:
                start = mid+1
            else:
                end = mid-1
        return Solution.ans