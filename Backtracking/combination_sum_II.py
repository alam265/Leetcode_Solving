class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        candidates.sort()
        def backtrack(i, ans, total):
            if total == target:
                res.append(ans.copy()) 
                return
            if i >= len(candidates) or total > target:
                return 

            ans.append(candidates[i]) 
            backtrack(i+1, ans, total + candidates[i]) 

            ans.pop() 

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, ans, total) 

        backtrack(0, [], 0) 
        return res 