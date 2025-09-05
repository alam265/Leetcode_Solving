class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        dic1 = {}
        dic2 = {} 
        

        for ch in s1:
            dic1[ch] = 1 + dic1.get(ch, 0)

        l = 0
        curr = s2[l] 
        for r in range(len(s2)): 
            if (r - l + 1) > len(s1): 
                if dic2[curr] > 0:
                    dic2[curr] -= 1 
                    if dic2[curr] == 0:
                        dic2.pop(curr)
                l+=1
                curr = s2[l]

            dic2[s2[r]] = 1 + dic2.get(s2[r], 0)
            
            if dic1 == dic2:
                return True
        return False