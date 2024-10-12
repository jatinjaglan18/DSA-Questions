import heapq
from collections import deque 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {}
        for i in tasks:
            freq[i] = 1 + freq.get(i, 0)
        
        maxheap = [-i for i in freq.values()]
        
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while maxheap or q:
            time += 1
            if len(maxheap) != 0:
                ele = 1 + heapq.heappop(maxheap)
                if ele != 0:
                    q.append([ele, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time