nums = [1,2,3,4,5,10,11,12,13,14,15,16]

nums = sorted(nums) 

numsWithoutRep = []

seen = set() 

for n in nums:
    if n not in seen:
        numsWithoutRep.append(n) 
    seen.add(n)

count = 1 
max_count = 1

for i in range(len(numsWithoutRep)-1):
    if numsWithoutRep[i+1] - numsWithoutRep[i] == 1:
        count += 1 
        max_count = max(count, max_count)
    else:
        count = 1


print(count)
  

"""OPtimal Solution"""


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums) 
#         longest = 0 

#         for n in nums:
#             if (n-1) not in numSet: 
#                 count = 0 
#                 while (n + count) in numSet: 
#                     count += 1 
#                 longest = max(count, longest)  

#         return longest
             
