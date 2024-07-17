class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat(piles,k,h):
            time = 0 
            for i in piles:
                time += (i+k-1) // k
               
            return time <= h
        
        low , high = 1, max(piles)
        
        while low < high:
            mid = (high + low) // 2
            
            if eat(piles,mid,h):
                high = mid
            else:
                low = mid+1
                
        return low
                
        
        