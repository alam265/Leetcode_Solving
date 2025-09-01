"""Brute Force"""
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)): 
#                 if nums[i] == nums[j] and abs(i-j) <= k:
#                     return True 
#         return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() 
        
        l=0 
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l]) 
                l+=1 
            if nums[r] in window:
                return True 
            window.add(nums[r])
        return False
    