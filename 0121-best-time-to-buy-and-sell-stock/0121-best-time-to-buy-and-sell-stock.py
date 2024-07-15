class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''stack = [0]
        nge = [len(prices)] * len(prices)
        for i in range(len(prices)):
            while prices[i] > prices[stack[-1]]:
                p = stack.pop()
                nge[p] = i
                if len(stack) == 0:
                    stack.append(i)
                    break
            else:
                stack.append(i)
        
        profit = 0
        for i in range(len(nge)):
            j = nge[i]
            while j < len(prices):
                p = prices[j]-prices[i]
                if p > profit:
                    profit = p    
                j = nge[j]'''
        
        
        profit = 0
        buy = prices[0]
        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > profit:
                profit = i - buy
                
            
        return profit
            
        
        
        