# strs = ["act","pots","tops","cat","stop","hat"] 

# res = [] 

# for i in range(len(strs)):
#     anagrams = [strs[i]]
#     if strs[i] != -1:
#         for j in range(i+1, len(strs)):
#             if strs[j] != -1 and sorted(strs[i]) == sorted(strs[j]):
#                 anagrams.append(strs[j])
#                 strs[j] = -1
#         res.append(anagrams)


# print(res)


"""Optimezed Solution """

strs = ["act","pots","tops","cat","stop","hat"]  
 
res = {} 

for word in strs:
    count = [0] * 26 
    for ch in word: 
        count[ord(ch) - ord("a")] += 1 

    if tuple(count) not in res: 
        res[tuple(count)] = [word]

    else:
         res[tuple(count)].append(word)


print(res.values())