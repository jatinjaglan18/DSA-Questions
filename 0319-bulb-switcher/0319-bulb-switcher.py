class Solution:
    def bulbSwitch(self, n: int) -> int:
        s = 0
        for i in range(1,n+1):
            if (i * i) <= n:
                s+=1
            else:
                break
        return s 
                
            
            
        