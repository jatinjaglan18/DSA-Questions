class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''if k > len(nums):
            k = k % len(nums)
        for i in range(k):
            val = nums.pop()
            nums.insert(0, val)
        return nums'''
        
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        