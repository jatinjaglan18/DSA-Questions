class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                i +=2
            else:
                i += 1

        f = []
        l = []
        for i in nums:
            if i == 0:
                l.append(i)
            else:
                f.append(i)
        return f + l

