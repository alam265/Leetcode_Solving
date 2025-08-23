class Solution:
    def is_palindrome(self, l, r, string): 
        while l < r: 
            if string[l] != string[r]: 
                return False 
            l += 1
            r -= 1
        return True 

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1 

        while l < r: 
            if s[l] != s[r]: 
                return self.is_palindrome(l+1, r, s) or self.is_palindrome(l, r-1 ,s)
            l += 1
            r -= 1

        return True 
        