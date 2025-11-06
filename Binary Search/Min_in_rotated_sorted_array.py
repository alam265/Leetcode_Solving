class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1 
        ans = nums[0]
        while l<= r: 
            if nums[l] < nums[r]: 
                ans = min(nums[l], ans) 
                break
            m = (l + r) // 2 
            ans = min(nums[m], ans)
            if nums[l] <= nums[m]:
                l = m + 1 
            else: 
                r = m - 1 

        return ans  

        