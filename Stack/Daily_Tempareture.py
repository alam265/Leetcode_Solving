class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] 

        for i in range(len(temperatures)): 
            while stack and stack[-1][0] < temperatures[i]: 
                val, idx = stack.pop() 
                diff = i - idx  
                res[idx] = diff 

            else:
                stack.append((temperatures[i], i))  
        return res
        




# temperatures = [30,38,30,36,35,40,28] 

# res = [] 

# for i in range(len(temperatures)):
#     flag = False
#     for j in range(i+1, len(temperatures)): 
#         if temperatures[j] > temperatures[i]: 
#             res.append(j-i)
#             flag = True
#             break 
            
#     if flag == False:
#         res.append(0)
    

# print(res)