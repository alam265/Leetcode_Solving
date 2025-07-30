nums = [2,2,1,3]
dictCount = {} 

for n in nums: 
    if n in dictCount: 
        dictCount[n] += 1 
    else: 
        dictCount[n] = 1
    newdict = {}
    if len(dictCount) > 2: 
        for k, v in dictCount.items(): 
            dictCount[k] -= 1 
        for k,v in dictCount.items(): 
            if dictCount[k] > 0: 
                newdict[k] = v 
        dictCount = newdict


res = []

for n in dictCount: 
    if nums.count(n) > len(nums) // 3: 
        res.append(n)
print(res)

print(dictCount)

