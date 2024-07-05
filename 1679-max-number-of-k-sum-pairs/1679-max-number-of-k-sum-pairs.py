class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = sorted(nums)
        l = 0
        r = len(nums) - 1
        ops = 0
        while l < r:
            num = k - n[l]
            
            if n[r] > num:
                r -= 1
            elif n[r] == num:
                ops += 1
                l+=1
                r-=1
            elif n[r] < num:
                l += 1
                
        return ops