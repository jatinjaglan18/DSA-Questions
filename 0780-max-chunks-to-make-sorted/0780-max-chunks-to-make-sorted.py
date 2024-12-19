class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = 0
        expected_sum = 0
        prefix_sum = 0
        for i, num in enumerate(arr):
            expected_sum += i
            prefix_sum += num
            if prefix_sum == expected_sum:
                cnt += 1 
        return cnt