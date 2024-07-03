class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # = [0 for i in range(len(candies))]
        maxm = max(candies)
        l = []
        '''for i in candies:
            if i > maxm:
                maxm = i'''
        
        for o in range(len(candies)):
            
            candies[o] += extraCandies
            if candies[o] >= maxm :
                l.append(True)
            else:
                l.append(False)
                
        return l
                
                
                
        
                