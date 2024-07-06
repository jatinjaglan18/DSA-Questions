class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        s = sum(nums[0:k])
        max_avg =  s / k
        print(max_avg)
        i = 1
        j = i + k
        while j<= len(nums):
            s = s - nums[i-1] + nums[j-1]
            val = s / k
            print(val)
            if max_avg < val :
                max_avg = val
            
            i += 1
            j += 1
        return max_avg 
                
        
            