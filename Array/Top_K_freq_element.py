"""Brute Force"""

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dic = {} 
#         ans = []

#         for n in nums: 
#             if n not in dic:
#                 dic[n] = 1
#             else: 
#                 dic[n] += 1 


#         sorted_lst = sorted(dic.items(), key = lambda x:x[1], reverse=True)
#         for i in range(k):
#             ans.append(sorted_lst[i][0])
#         return ans

        
# print(ans)


"""Optimal Solution""" 

nums = [1,1,1,2,2,3] 
k = 2

dic = {} 
count_bucket = [[] for i in range(len(nums)+1)] 
ans = []

for n in nums:
    if n not in dic: 
        dic[n] = 1 
    else: 
        dic[n] += 1 

for number, count in dic.items(): 
    count_bucket[count].append(number) 


for i in range(len(count_bucket)-1, 0, -1): 
    for n in count_bucket[i]: 
        ans.append(n) 


print(ans)
