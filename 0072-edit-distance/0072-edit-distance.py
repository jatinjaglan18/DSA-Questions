class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for j in range(len(word1) + 1)] for i in range(len(word2) + 1)]
        
        for i in range(1,len(dp)):
            dp[i][0] = i
        for j in range(1,len(dp[0])):
            dp[0][j] = j
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word2[i-1] == word1[j-1]:
                    val = 0
                else:
                    val = 1
                
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + val)
              
        return dp[-1][-1]