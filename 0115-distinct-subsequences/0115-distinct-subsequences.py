class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(t) + 1)] for i in range(len(s)+1)]
        dp[0][0] = 1
        
        for i in range(1, len(s) + 1):
            dp[i][0] = 1
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1] == t[j-1] and dp[i-1][j-1]:
                    dp[i][j] = max(dp[i-1][j-1] + dp[i-1][j], dp[i-1][j] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]