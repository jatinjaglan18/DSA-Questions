class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        i = nums[0]
        res = self.subsets(nums[1:])
        ans = []
        for j in res:
            ans.append(j)
            ans.append([i]+j)
            
        return ans
        