class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplet = set()
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            f = nums[i]
            j = i + 1
            k = len(nums)-1
            
            while j < k :
                
                s = nums[j]
                t = nums[k]
                
                val = f + s + t 
                
                if val < 0:
                    j += 1
                elif val > 0:
                    k -= 1
                    
                else :
                    triplet.add((f,s,t))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                        

        return triplet
                    
                
                    