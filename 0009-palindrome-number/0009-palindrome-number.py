class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r_s = ''
        for i in range(len(s)-1,-1,-1):
            r_s = r_s + s[i]
        return s == r_s
    
        