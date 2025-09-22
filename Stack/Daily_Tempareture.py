temperatures = [30,38,30,36,35,40,28] 

res = [] 

for i in range(len(temperatures)):
    flag = False
    for j in range(i+1, len(temperatures)): 
        if temperatures[j] > temperatures[i]: 
            res.append(j-i)
            flag = True
            break 
            
    if flag == False:
        res.append(0)
    

print(res)