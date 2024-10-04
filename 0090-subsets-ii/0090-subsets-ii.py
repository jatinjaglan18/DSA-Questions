class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(nums):
            if len(nums) == 0:
                return [[]]
            ch = nums[0]
            ans = backtrack(nums[1:])
            res = []
            for i in ans:
                if i not in res:
                    res.append(i)
                if [ch] + i not in res:
                    res.append([ch] + i)

            return res 
        return backtrack(nums)