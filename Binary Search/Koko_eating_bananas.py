"""Brute Force"""

# import math
# piles=[25,10,23,4]
# h=4

# rate = 1 

# while True: 
#     total_time = 0
#     for p in piles: 
#         total_time += math.ceil(p/rate) 

#     if total_time <= h: 
#         print(rate) 
#         break 
#     rate += 1 

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = 0
        while l<=r: 
            rate = (l+r) // 2  
            total_hour = 0
            for p in piles: 
                total_hour += math.ceil(p/rate) 

            if total_hour <= h: 
                ans = rate
                r = rate - 1 
            else: 
                l = rate + 1 
        return ans










