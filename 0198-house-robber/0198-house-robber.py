class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for i in range(len(nums))]
        
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[i-1],nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]