class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        cnt = [0]*(n + 1)
        current_sum = 0
        k = 0
        for i in range(n):
            while (current_sum + cnt[i] < nums[i]):
                if k == len(queries):
                    return -1
                l, r, val = queries[k]
                k += 1
                if r < i:
                    continue
                cnt[max(l,i)] += val
                cnt[r+1] -= val
            current_sum += cnt[i]
        return k