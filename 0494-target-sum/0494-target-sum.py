class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2 != 0 or sum(nums) + target < 0:
            return 0

        subset_sum = (sum(nums) + target) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        print(subset_sum)
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
            print(dp)
        return dp[subset_sum]
        