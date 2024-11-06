class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        naturalsum = (s*(s+1)) / 2
        nsum = sum(nums)
        return int(naturalsum - nsum)