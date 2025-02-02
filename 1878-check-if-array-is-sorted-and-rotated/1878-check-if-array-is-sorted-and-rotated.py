class Solution:
    def check(self, nums: List[int]) -> bool:
        n = sorted(nums)
        if nums == n:
            return True
        arr1 = []
        arr2 = []
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                arr1 = nums[:i+1]
                arr2 = nums[i+1:]
                break
        return (n == arr2 + arr1)
            