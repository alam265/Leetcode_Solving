ops = ["5","2","C","D","+"] 

res = [] 

for elem in ops:
    if elem == "C": 
        res.pop() 
    elif elem == "D": 
        res.append(int(res[-1])*2) 

    elif elem =="+": 
        res.append(int(res[-1]) + int(res[-2]))
    
    else:
        res.append(int(elem))

print(sum(res))
