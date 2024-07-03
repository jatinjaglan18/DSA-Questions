class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        a = 2**31
        b = 2**31
        for i in nums:
            if i <= a:
                a = i
            elif i <= b:
                b = i
            else :
                return True
            
        return False

            
            

