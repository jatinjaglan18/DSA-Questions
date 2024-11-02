class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_curr = nums[0]
        max_curr = nums[0]
        max_hist = nums[0]
        
        for i in nums[1:]:
            min_curr, max_curr = min(min_curr*i, max_curr*i, i), max(min_curr*i, max_curr*i, i)
            max_hist = max(max_hist, max_curr)
        
        return max_hist