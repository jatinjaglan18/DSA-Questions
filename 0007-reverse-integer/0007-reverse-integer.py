class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31:
            return 0
        num = 0
        
        n = abs(x)
        while n > 0:
            rem = n % 10
            num = num*10 + rem 
            n = n // 10
           
        if num < -2**31 or num > 2**31:
            return 0
        
        if x - abs(x) == 0:
            return num
        else:
            return -num