class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        dic1 = {}
        dic2 = {} 
        

        for ch in s1:
            dic1[ch] = 1 + dic1.get(ch, 0)

        l = 0
       
        for r in range(len(s2)): 
            if (r - l + 1) > len(s1): 
                if dic2[s2[l]] > 0:
                    dic2[s2[l]] -= 1 
                    if dic2[s2[l]] == 0:
                        dic2.pop(s2[l])
                l+=1


            dic2[s2[r]] = 1 + dic2.get(s2[r], 0)
            
            if dic1 == dic2:
                return True
        return False