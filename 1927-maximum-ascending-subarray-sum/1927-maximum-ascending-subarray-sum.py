class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                curr_sum += nums[i]
            else:
                max_sum = max(max_sum,curr_sum)
                curr_sum = nums[i]

        max_sum = max(max_sum,curr_sum) 
        return max_sum