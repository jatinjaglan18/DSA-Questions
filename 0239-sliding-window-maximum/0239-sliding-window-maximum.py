class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        l = 0
        res=[]
        for i in range(len(nums)):
            
            while len(q) != 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if l > q[0]:
                q.pop(0)
            
            if i + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            
            
        return res