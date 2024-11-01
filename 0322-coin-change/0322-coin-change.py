class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [(amount+1) for i in range(amount+1)]
        min_coin[0] = 0
        
        for i in range(len(min_coin)):
            for coin in coins:
                if i - coin >= 0:
                    min_coin[i] = min(min_coin[i], 1 + min_coin[i - coin])
                    
        if min_coin[-1] == amount+1:
            return -1
        return min_coin[-1]
                    