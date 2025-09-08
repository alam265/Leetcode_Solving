class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = len(nums)+1
        
        l=0
        total = 0
        for r in range(len(nums)):
            total += nums[r] 
            while total >= target: 
                min_size = min(min_size, r - l + 1) 
                total -= nums[l] 
                l += 1 

        return 0 if min_size == len(nums)+1 else min_size



        
        





