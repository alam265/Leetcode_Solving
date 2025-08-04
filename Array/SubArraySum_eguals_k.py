nums = [2,-1,1,2]
k = 2

# ans = 0 

# for i in range(len(nums)):
#     total = 0
#     for j in range(i, len(nums)): 
#         total += nums[j] 
#         if total == k: 
#             ans+=1 
        


# print(ans)


"""Optimal Solution""" 


dic = {0:1} 

prefix_sum = 0 

count = 0

for n in nums: 
    prefix_sum += n 
    if (prefix_sum - k) in dic: 
        count += dic[prefix_sum - k] 
    
    if prefix_sum not in dic:
        dic[prefix_sum] = 1 
    else:
        dic[prefix_sum] += 1 


print(count)


