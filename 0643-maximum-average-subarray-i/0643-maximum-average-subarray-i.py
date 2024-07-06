class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        s = 0
        for i in range(k):
            s += nums[i]
        
        max_sum = s
        i = 1
        j = i + k
        while j<= len(nums):
            s = s - nums[i-1] + nums[j-1]
            if max_sum < s :
                max_sum = s
            
            i += 1
            j += 1
        return max_sum / k
                
        
            