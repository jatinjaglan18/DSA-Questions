from queue import PriorityQueue 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for i in nums:
            if pq.qsize() < k:
                pq.put(i)
            else:
                val = pq.get()
                if val < i:
                    pq.put(i)
                else:
                    pq.put(val)
                    
        return pq.get()