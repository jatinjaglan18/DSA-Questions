class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        '''memo = {}
        
        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else: 
                    return 0
            
            if (i,total) in memo:
                return memo[(i,total)]
            
            add = backtrack(i+1, total + nums[i])
            subtract = backtrack(i+1, total - nums[i])
            
            memo[(i,total)] = add + subtract
            
            return memo[(i,total)]
        
        return backtrack(0,0)'''
        
        if (sum(nums) + target) % 2 != 0 or sum(nums) + target < 0:
            return 0

        subset_sum = (sum(nums) + target) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[subset_sum]
                