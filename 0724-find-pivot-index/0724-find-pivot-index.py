class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = [0 for i in range(len(nums))]
        rsum = [0 for i in range(len(nums))]
        l = 0
        r = len(nums) - 1
        
        for i in range(1,len(nums)):
            lsum[i] = lsum[i-1] + nums[i-1]
            
        for i in range(len(nums)-2,-1,-1):
            rsum[i] = rsum[i+1] + nums[i+1]
            
        for i in range(len(nums)):
            if rsum[i] == lsum[i]:
                return i
        else:
            return -1