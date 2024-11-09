class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
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
        
        return backtrack(0,0)