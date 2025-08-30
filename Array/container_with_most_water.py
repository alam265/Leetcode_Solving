"""Brute Force"""
# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         max_water = 0
#         for i in range(len(heights)):
#             for j in range(i+1, len(heights)): 
#                 w = j - i 
#                 h = min(heights[i], heights[j]) 
#                 max_water = max(max_water, w*h) 

#         return max_water
    


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1 

        while l < r: 
            w = r - l 
            h = min(heights[l], heights[r]) 
            max_area = max(max_area, w*h) 
            if heights[r] > heights[l]: 
                l +=1 
            else:
                r -= 1 

        return max_area