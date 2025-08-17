"""Naive Approach"""

def first_missing_positive(nums): 
    for i in range(1, len(nums)+1): 
        if i not in nums: 
            return i 

nums = [-2,-1,0]

print(first_missing_positive(nums))






