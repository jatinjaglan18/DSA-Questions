class Solution:
    def countBits(self, n: int) -> List[int]:
        '''ans = []
        for i in range(n+1):
            count = 0
            while i > 0 :
                if i % 2 == 1:
                    count += 1
                i = i // 2
            ans.append(count)
        return ans'''
        
        if n<=1:
            if n == 0 :
                return [0]
            else:
                return [0,1]
					
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            if i%2==0:
                val = i//2
                dp[i] = dp[val]
					# val its basically i<<2
                    
            else:
                dp[i] = dp[i-1]+1
                
                
        return dp