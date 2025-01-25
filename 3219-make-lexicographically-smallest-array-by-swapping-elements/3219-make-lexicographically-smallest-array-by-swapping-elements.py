class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        srt = sorted((nums[i], i) for i in range(n))
        i = 0

        while i < n:
            idx = [srt[i][1]]
            j = i+1
            while j < n and abs(srt[j][0] - srt[j-1][0]) <= limit:
                idx.append(srt[j][1])
                j += 1
            if j > i+1:
                idx.sort()
                for k in range(len(idx)):
                    nums[idx[k]] = srt[i+k][0]
            i = j

        return nums