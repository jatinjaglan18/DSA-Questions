class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        qb = [0 for i in range(n+1)]
        qb[1] = 1
        qb[2] = 1
        
        def tfib(n,qb):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            if qb[n] != 0:
                return qb[n]
            
            f1 = tfib(n-1,qb)
            f2 = tfib(n-2,qb) 
            f3 = tfib(n-3,qb)
            ans = f1+f2+f3
            qb[n] = ans
            return ans
        
        return(tfib(n,qb))
        