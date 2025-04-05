class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total |= num  # Step 1: Compute bitwise OR of all numbers
        return total * (1 << (len(nums) - 1))