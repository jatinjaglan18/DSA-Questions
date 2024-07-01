class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''s = str(x)
        r_s = ''
        for i in range(len(s)-1,-1,-1):
            r_s = r_s + s[i]
        return s == r_s
        
        rev_num = 0
        n = abs(x)
        while n > 0:
            rem = n % 10
            rev_num = rev_num*10 + rem
            n = n // 10
            
        if x - abs(x) !=0:
            rev_num = -rev_num
            return False
            
        return rev_num == x '''
        
        x = str(x)
        return x == x[::-1]
            
    
        