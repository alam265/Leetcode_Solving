class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        dicS ={} 
        for i in s: 
            if i in dicS:
                dicS[i] += 1 
            else:
                dicS[i] = 1

        dicT ={} 
        for j in t: 
            if j in dicT:
                dicT[j] += 1 
            else:
                dicT[j] = 1 

        return dicS == dicT