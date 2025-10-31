class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 

        while l <= r: 
            mid = (l+r)//2 
            if target == nums[mid]: 
                return mid 
            elif nums[l] <= nums[mid]: 
                if target < nums[l] or target > nums[mid]:
                    l = mid+1 
                elif target < nums[mid] and target >= nums[l]: 
                    r = mid-1 

            else: 
                if target < nums[mid] or target > nums[r]: 
                    r = mid - 1 
                elif target > nums[mid] and target <= nums[r]:
                    l = mid + 1
        return -1

                
        