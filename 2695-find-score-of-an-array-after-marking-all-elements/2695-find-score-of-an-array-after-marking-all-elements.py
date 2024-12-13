import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        order = list(enumerate(nums))
        (order.sort(key = lambda x : x[1] ))
        visit = set()
        ans = 0
        for i in order:
            if i[0] in visit:
                continue
            ans += i[1]
            visit.add(i[0])
            if i[0] > 0:
                visit.add(i[0]-1)
            if i[0] + 1 < len(nums):
                visit.add(i[0]+1)
        return ans

