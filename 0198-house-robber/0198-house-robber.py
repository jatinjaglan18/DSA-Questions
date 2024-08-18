class Solution:
    def rob(self, nums: List[int]) -> int:
        oinc = nums[0]
        oexc = 0
        
        for i in range(1,len(nums)):
            ninc = oexc + nums[i]
            nexc = max(oinc,oexc)
            
            oinc = ninc
            oexc = nexc
            
        return max(oinc,oexc)