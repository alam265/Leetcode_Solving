# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         res="" 

#         for s in strs: 
#             res += "|" + s

#         return res

#     def decode(self, s: str) -> List[str]:
#         lst = s.split("|")[1:] 
#         return lst


"""Another Solution"""

strs = [""] 


res = "" 

for s in strs: 
    res += str(len(s))  + s 


print(res)

lst = []  


i = 0  

while i < len(res):
    st = "" 
    length = int(res[i]) 
    for j in range(i+1, i+1+length):
        st += res[j] 

    lst.append(st) 
    i = i + length +1


print(lst) 



