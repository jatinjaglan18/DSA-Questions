class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        def getnext(num):
            res = 0
            for i in str(num):
                res += int(i) ** 2
            
            return res
        
        while n != 1 and n not in visit:
            visit.add(n)
            n = getnext(n)
        
        return n == 1