class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)): 
            rem = target - nums[i] 
            if rem in dic: 
                return [dic[rem], i]
            dic[nums[i]] = i 








