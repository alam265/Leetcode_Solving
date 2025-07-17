""" Naive Approach"""
nums = [1,2,4,6]

ans = [] 

for i in range(len(nums)):
    product = 1 
    for j in range(len(nums)): 
        if i != j:
            product *= nums[j] 
    ans.append(product) 

print(ans)