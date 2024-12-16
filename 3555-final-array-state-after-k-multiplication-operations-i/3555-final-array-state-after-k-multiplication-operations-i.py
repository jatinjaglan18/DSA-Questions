import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = []
        for i in range(len(nums)):
            n.append([nums[i], i])
        #print(n)
        heapq.heapify(n)
        for i in range(k):
            val=heapq.heappop(n)
            ele = val[0] * multiplier
            nums[val[1]] = ele
            heapq.heappush(n, [ele,val[1]])
        return nums
        
        