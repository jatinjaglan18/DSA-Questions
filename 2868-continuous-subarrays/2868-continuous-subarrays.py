class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = i = 0
        d = dict()
        for j,n in enumerate(nums):
            nd = d.copy()
            for k,v in nd.items():
                if abs(k-n) > 2:
                    i = max(i,v+1)
                    d.pop(k)
            d[n] = j
            res += j - i + 1
        return res