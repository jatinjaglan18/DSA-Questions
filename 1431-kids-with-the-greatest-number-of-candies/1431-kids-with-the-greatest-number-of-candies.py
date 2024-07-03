class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = [0 for i in range(len(candies))]
        maxm = 0
        
        for i in candies:
            if i > maxm:
                maxm = i
        
        for o in range(len(candies)):
            
            candies[o] += extraCandies
            if candies[o] >= maxm :
                l[o] = True
            else:
                l[o] = False
                
        return l
                
                
                
        
                