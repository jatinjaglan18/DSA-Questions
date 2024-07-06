class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        count_0 = 0
        length = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_0 += 1
                
            while count_0 > 1:
                if nums[l] == 0:
                    count_0 -= 1
                    
                l += 1    
                
            if length < (r - l + 1 - count_0):
                length = (r - l + 1 - count_0)
        
        if length  == len(nums):
            return length - 1
        else:
            return length