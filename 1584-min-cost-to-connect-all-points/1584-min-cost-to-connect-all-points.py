import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        d = {}
        min_cost = 0
        heap = [(0,0)]
        
        while heap:
            w,u = heapq.heappop(heap)
            
            if u in visited:
                continue
            
            visited.add(u)
            min_cost += w
            
            for v in range(n):
                if v not in visited:
                    dist = (abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1]))
                    
                    if dist < d.get(v, float('inf')):
                        d[v] = dist
                        heapq.heappush(heap, (dist,v))
        return min_cost