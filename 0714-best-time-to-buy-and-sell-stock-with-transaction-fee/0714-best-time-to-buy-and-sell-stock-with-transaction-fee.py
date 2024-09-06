class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        obsp = -prices[0]
        ossp = 0
        
        for i in range(1, len(prices)):
            nbsp = 0
            nssp = 0
            
            if ossp - prices[i] > obsp:
                nbsp = ossp - prices[i]
            else:
                nbsp = obsp
            
            if prices[i] + obsp - fee > ossp:
                nssp = prices[i] + obsp - fee
            else:
                nssp = ossp
                
            obsp = nbsp
            ossp = nssp
        
        return ossp