class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)

        while low < high:
            mid = (low+high) // 2
            if sum([((n-1) // mid) for n in nums]) <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return high