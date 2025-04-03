class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max = [nums[0]] * len(nums)
        suffix_max = [nums[-1]] * len(nums)

        for i in range(1,len(nums)):
            prefix_max[i] = max(nums[i], prefix_max[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i+1])
        

        ans = 0
        for i in range(1,len(nums)-1,1):
            val = (prefix_max[i-1] - nums[i]) * suffix_max[i+1]
            ans = max(ans, val)
        return ans