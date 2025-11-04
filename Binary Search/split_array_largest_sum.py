class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            noArr = 1
            currSum = 0 
            for n in nums:
                currSum += n 
                if currSum > largest:
                    noArr += 1 
                    currSum = n 
            return noArr <= k 


        ans = 0
        l, r = max(nums), sum(nums)
        while l <= r: 
            mid = (l+r) // 2 
            if canSplit(mid): 
                ans = mid 
                r = mid - 1 
            else:
                l = mid + 1 

        return ans