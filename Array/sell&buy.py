prices = [7,1,5,3,6,4] 

l = 0        #buy
r = 1       #sell 

maxProfit = 0 

while r < len(prices): 
    profit = prices[r] - prices[l]
    if profit < 0 :  
        l = r 
        
    maxProfit = max(profit, maxProfit) 
    r += 1


print(maxProfit)



"""Another Soln"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(1, len(prices)): 
            if prices[l] > prices[r]:
                l = r 

            profit = max(profit, prices[r]-prices[l])

        return profit