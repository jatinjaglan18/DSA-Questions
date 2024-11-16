class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a=b=0
        for i in num1:
            a = a*10+(ord(i) - 48)
        for i in num2:
            b = b*10+(ord(i) - 48)
        
        return str(a*b)
        
        '''num1 = int(num1)
        num2 = int(num2)
        
        return str(num1*num2)'''