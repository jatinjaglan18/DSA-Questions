def gcd(s,l):
    if l % s == 0:
        return s
    
    return gcd(l%s,s)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        l = nums[0]
        s = nums[0]
        for i in nums:
            if i > l:
                l = i
                
            if i < s :
                s = i
                
        return gcd(s,l)
        
                