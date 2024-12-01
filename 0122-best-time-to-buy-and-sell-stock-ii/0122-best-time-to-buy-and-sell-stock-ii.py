class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]

        profit = 0

        for i in range(1,len(prices)):
            if prices[i] >= sell:
                sell = prices[i]
            
            else:
                profit += sell - buy
                buy = prices[i]
                sell = prices[i]
        profit += sell-buy
        return profit