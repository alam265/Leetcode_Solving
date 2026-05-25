class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        def helper(ans, i, total): 
            
            if total == target:
                res.append(ans.copy())
                return 
            if total > target or i >= len(nums):
                return 


            ans.append(nums[i])

            helper(ans, i, total + nums[i]) 
            ans.pop()
            helper(ans, i+1, total)

        helper([], 0, 0) 
        return res 