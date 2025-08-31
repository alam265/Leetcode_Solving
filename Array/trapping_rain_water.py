class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        
        n = len(height)
        
        leftmax = [0]*n
        rightmax = [0]*n

        leftmax[0] = height[0]
        rightmax[n-1] = height[n-1]

        for i in range(1, n): 
            leftmax[i] = max(leftmax[i-1], height[i]) 


        for j in range(n-2, -1, -1): 
            rightmax[j] = max(rightmax[j+1], height[j]) 


        for i in range(n): 
            res += min(leftmax[i], rightmax[i]) - height[i]

        return res