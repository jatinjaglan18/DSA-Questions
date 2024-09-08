class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time - O(n)
        # space - O(n)
        '''d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
            
        for i in d.keys():
            if d[i] == 1:
                return i'''
        
        # Time - O(n)
        # space - O(n)
        #X-OR gate
        xr = 0
        for i in nums:
            xr ^= i  
        return xr