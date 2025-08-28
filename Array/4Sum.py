nums = [3,2,3,-3,1,0]
target = 3
res= []

nums.sort()
for i in range(len(nums)): 
    if i > 0 and nums[i] == nums[i-1]: 
        continue 
    for j in range(i+1 ,len(nums)): 
        if j > i+1 and nums[j] == nums[j-1]: 
            continue 
        l, r = j+1, len(nums)-1 
        while l < r: 
            four_sum = nums[i] + nums[j] + nums[l] + nums[r] 
            if four_sum < target: 
                l += 1
            elif four_sum > target: 
                r -= 1 
            elif four_sum == target:
                res.append([nums[i] ,nums[j] ,nums[l] ,nums[r]])
                l += 1 
                while nums[l] == nums[l-1] and l < r: 
                    l += 1 

print(res)
# Output: [[-3,0,3,3],[-3,1,2,3]] 