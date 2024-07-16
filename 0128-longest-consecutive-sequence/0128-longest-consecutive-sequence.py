class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        
        count = 0
        for i in n:
            
            if i - 1 in n:
                continue
            
            elif i - 1 not in n:
                counter = 0
                
                while i in n:
                    i += 1
                    counter += 1
                    
            
                count = max(count,counter)
            
        return count