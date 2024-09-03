class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost)+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(dp),1):
            val = min(dp[i-1],dp[i-2])
            if i == len(cost):
                dp[i] = val
            else:
                dp[i] = val + cost[i]
        
        return dp[-1]