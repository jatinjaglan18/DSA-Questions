class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = float((len(nums)) / 2)
        
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = d.get(i,1)
            else:
                d[i] += 1
        
        
        for i in d.keys():
            if d[i] > a :
                 return i
            