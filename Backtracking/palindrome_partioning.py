class Solution:
    def isPalindrome(self, string):
        return string == string[::-1]


    def getAllPart(self, s, res, part):
        if len(s) == 0:
            res.append(part.copy())
            return 

        for i in range(len(s)): 
            if self.isPalindrome(s[:i+1]):
                part.append(s[:i+1])
                self.getAllPart(s[i+1:], res, part) 
                part.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        part = [] 
        self.getAllPart(s, res, part)
        return res