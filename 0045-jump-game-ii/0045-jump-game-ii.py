class Solution:
    def jump(self, nums: List[int]) -> int:
        near = 0
        ans = 0
        far = 0
        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
                
            near = far + 1
            far = farthest
            ans += 1
        return ans