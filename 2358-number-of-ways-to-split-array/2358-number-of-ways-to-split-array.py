class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        left_sum[0] = nums[0]
        right_sum[-1] = nums[-1]
        for i in range(1,n):
            left_sum[i] = left_sum[i-1] + nums[i]
        for i in range(n-2,-1,-1):
            right_sum[i] = right_sum[i+1] + nums[i]
        
        ans = 0
        for i in range(n-1):
            if left_sum[i] >= right_sum[i+1]:
                ans+=1

        return ans