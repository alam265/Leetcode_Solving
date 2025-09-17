class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
    
        for elem in s: 
            if elem == "}":
               
                if stack and stack[-1] == "{" :
                    stack.pop() 
                else:
                    return False
                    
            elif elem == "]":
          
                if stack  and stack[-1] == "[" :
                    stack.pop() 
                else:
                    return False
              
            elif elem == ")":
    

                if stack and stack[-1] == "(": 
                    stack.pop() 
                else:
                    return False
   

            else: 
                stack.append(elem) 


        if len(stack) == 0: 
            return True 
        else:
            return False



        