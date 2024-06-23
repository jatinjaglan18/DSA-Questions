class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = sorted(nums)
        z = k-1
        return l[-k]