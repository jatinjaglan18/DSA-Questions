class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        mi = 0
        ma = 0
        for num in nums:
            prefix += num
            mi = min(mi, prefix)
            ma = max(ma,prefix)
        
        return ma - mi

        