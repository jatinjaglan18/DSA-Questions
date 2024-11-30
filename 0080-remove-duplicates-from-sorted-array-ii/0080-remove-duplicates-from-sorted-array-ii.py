class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i+1]:
                count += 1
            #print(count)
            
            if nums[i] != nums[i+1]:
                count = 1
            
            if count > 2:
                nums.remove(nums[i])
        return len(nums)
            