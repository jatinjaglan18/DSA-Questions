class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0
        
        for i in range(k+1):
            temp = dp.copy()
            
            for s, d, c in flights:
                if dp[s] == float('inf'):
                    continue
                
                if dp[s] + c < temp[d]:
                    temp[d] = dp[s] + c
                
            dp = temp
        
        if dp[dst] == float('inf'):
            return -1
        return dp[dst]