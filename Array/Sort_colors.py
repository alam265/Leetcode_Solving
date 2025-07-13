nums = [1,0,1,2]

l = 0 
r = len(nums)-1 

i = 0 

while i <= r: 
    if nums[i] == 0: 
        nums[i], nums[l] = nums[l], nums[i]      #swap
        i += 1
        l += 1

    elif nums[i] == 2: 
        nums[i], nums[r] = nums[r], nums[i]  #swap
        r -= 1  
    else: 
        i += 1


print(nums)


