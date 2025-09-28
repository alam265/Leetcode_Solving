
"""Brute Force"""
heights = [2,1,5,6,2,3] 
area = 0
for i in range(len(heights)): 
    for j in range(i+1, len(heights)):
        h = min(heights[i:j+1])
        w = j - i +1
        area = max(area, h*w) 


print(area)


"""Optimal"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 

        area = 0

        left, right = [0]*len(heights), [0]*len(heights) 

        # Right Smaller 
        for i in range(len(heights)-1, -1, -1): 
            while stack  and heights[i] <= heights[stack[-1]]: 
                stack.pop() 

            right[i] = stack[-1] if stack else len(heights) 
            stack.append(i)

        while stack:
            stack.pop() 


        # Left smaller 
        for j in range(len(heights)): 
            while stack and heights[j] <= heights[stack[-1]]: 
                stack.pop() 

            left[j] = stack[-1] if stack else -1 
            stack.append(j) 


        for k in range(len(heights)): 
            h = heights[k] 
            w = right[k] - left[k] - 1 
            area = max(area, h*w)  

        return area

        