class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''for i in range(len(prices)-1):
            j = i+1
            while j < len(prices) and prices[j] > prices[i]:
                j += 1
                if j == len(prices):
                    break
            else:
                prices[i] -= prices[j]
        return prices'''
        stack = []
        ans = prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                ans[stack.pop()] -= prices[i]
            stack.append(i)
        return ans
