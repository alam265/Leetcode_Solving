class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  
        path = path.split("/") 

        for curr in path:
            if curr == "..": 
                if stack:
                    stack.pop() 
            elif curr == "." or curr == "":
                continue 
            else:
                stack.append(curr) 
        return "/" + "/".join(stack)



        