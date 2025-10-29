class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) 
        ans = 0

        def canShip(cap): 
            ships = 1 
            currentCap = cap
            for w in weights: 
                if currentCap - w < 0:
                    ships += 1
                    currentCap = cap 
                currentCap -= w 
            return ships <= days 


        while l <= r: 
            mid = (l+r) //2 
            if canShip(mid): 
                ans = mid 
                r = mid - 1 
            else: 
                l = mid + 1 

        return ans

        