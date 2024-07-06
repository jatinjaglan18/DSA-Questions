class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = 0
        l = 0
        
        count_0 = 0
        for r in range(len(nums)):
            if nums[r]==0:
                count_0 += 1
                
            while count_0 > k:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1
           
            if length < (r-l+1):
                length = (r - l+1)
        
        return length
                