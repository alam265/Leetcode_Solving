def check(self, nums):



    count = 0 
    l = len(nums)
    for i in range(l):
        if nums[i] > nums[(i+1)%l]:
            count+=1

    if count > 1:
        return False 
    return True