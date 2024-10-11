import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for i in points:
            a = 0
            for j in i:
                a += j*j
            
            heapq.heappush(distances, [a] + i)
        
        res = []
        for i in range(k):
            ans = heapq.heappop(distances)
            res.append(ans[1:])
        
        return res