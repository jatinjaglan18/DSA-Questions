class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        
        dp = [0 for i in range(len(s)+1)]
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,len(s)+1,1):
            digit_1 = int(s[i-1])
            digit_2 = int(s[i-2:i])
            
            val = 0
            if digit_1 != 0:
                val += dp[i-1]
            if 10 <= digit_2 <= 26:
                val += dp[i-2]
                
            dp[i] = val
            
        return dp[-1]