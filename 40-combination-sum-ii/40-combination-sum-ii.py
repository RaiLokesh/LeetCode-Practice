class Solution:
    ans = 0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        Solution.ans = []
        visited = []
        def solve(curr_candidates, chosen_candidates):
            if not curr_candidates or [curr_candidates, chosen_candidates] in visited: return
            for i in range(len(curr_candidates)):
                if curr_candidates[i]+sum(chosen_candidates) <= target:
                    if curr_candidates[i]+sum(chosen_candidates) == target:
                        if chosen_candidates+[curr_candidates[i]] not in Solution.ans:
                            Solution.ans.append([i for i in chosen_candidates+[curr_candidates[i]]])
                    else:
                        solve(curr_candidates[i+1:], chosen_candidates+[curr_candidates[i]])
                else:
                    return
            visited.append([curr_candidates, chosen_candidates])
        solve(candidates, [])
        return Solution.ans