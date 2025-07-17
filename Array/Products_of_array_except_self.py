""" Naive Approach"""
nums = [1,2,4,6]

ans = [] 

for i in range(len(nums)):
    product = 1 
    for j in range(len(nums)): 
        if i != j:
            product *= nums[j] 
    ans.append(product) 

print(ans)


"""Optimal Solution"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums) 
        pref = 1 

        for i in range(len(nums)): 
            res[i] = pref 
            pref *= nums[i] 
             
        postfix = 1 

        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j] 

        return res 


        