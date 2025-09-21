class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        for a in asteroids:  
            while stack and stack[-1]> 0 and a < 0: 
                diff = a + stack[-1] 
                if diff > 0: 
                    break 
                elif diff < 0: 
                    stack.pop() 
                else: 
                    stack.pop()
                    break 
            else:
                stack.append(a)

        return stack
        