from queue import PriorityQueue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = PriorityQueue()
        for i in points:
            a = 0
            for j in i:
                a += j*j
            
            distances.put([a] + i)
        
        res = []
        for i in range(k):
            ans = distances.get()
            res.append(ans[1:])
        
        return res