class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
            
        for i in d.keys():
            if d[i] == 1:
                return i