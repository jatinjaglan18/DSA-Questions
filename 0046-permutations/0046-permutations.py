class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutations(nums,ans):
            if len(nums) == 0:
                res.append(ans)
                return 

            for i in range(len(nums)):
                ch = nums[i]
                nnums = nums[:i] + nums[i+1:]
                permutations(nnums,ans+[ch])
                
        permutations(nums,[])
        return res