class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        obs = -prices[0]
        oss = 0
        ocs = 0
        
        for i in range(1,len(prices)):
            nbs = 0
            nss = 0
            ncs = 0
            
            #buying state
            if ocs - prices[i] > obs:
                nbs = ocs - prices[i]
            else:
                nbs = obs
                
            #selling state
            if prices[i] + obs > oss:
                nss = prices[i] + obs
            else:
                nss = oss
            
            #cooldown state
            if oss > ocs:
                ncs = oss
            else:
                ncs = ocs
                
            obs = nbs 
            oss = nss
            ocs = ncs
        return oss