from queue import PriorityQueue
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        merged = []
        for i in range(len(nums1)):
            merged.append((nums2[i],nums1[i]))
        
        s = sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True)
        ksum = 0
        pq = []
        ans = 0 
        
        for i, j in s:
            ksum += i
            heapq.heappush(pq,i)
            
            if len(pq) == k :
                x = ksum * j
                
                if ans < x:
                    ans = x

                ksum -= heapq.heappop(pq)
            
        return ans
        
            
        
           
                
                
                
        
        
        
        
        