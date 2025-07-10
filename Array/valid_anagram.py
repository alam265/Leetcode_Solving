strs = ["act","pots","tops","cat","stop","hat"] 

res = [] 

for i in range(len(strs)):
    anagrams = [strs[i]]
    if strs[i] != -1:
        for j in range(i+1, len(strs)):
            if strs[j] != -1 and sorted(strs[i]) == sorted(strs[j]):
                anagrams.append(strs[j])
                strs[j] = -1
        res.append(anagrams)


print(res)