class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''i = 0
        
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            
            i += 1'''
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            else:
                i += 1
                