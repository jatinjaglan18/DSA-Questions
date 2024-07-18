class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
    
        while l <= h:
            m = (h+l)//2
            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1
                
                
        return nums[m]