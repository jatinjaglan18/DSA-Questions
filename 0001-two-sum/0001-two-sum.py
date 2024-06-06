class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force
        '''
        l = []
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    l.append(i)
                    l.append(j)
        
        return l'''
        
        #Using Hashmap
        d = {}
        for i in range(len(nums)):
            z = target - nums[i]
            
            if z not in d.keys():
                d[nums[i]] = d.get(nums[i], i)
            
            else: 
                return [d[z], i]
                
            