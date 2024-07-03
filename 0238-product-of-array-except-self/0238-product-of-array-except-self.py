class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums)-1):
            pre.append(pre[i] * nums[i])
        post = [0 for i in range(len(nums))]
        post[len(nums) - 1] = 1
        
        
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
    
        return res