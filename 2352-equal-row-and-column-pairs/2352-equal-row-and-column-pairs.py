class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        g1 = {}
        for i in grid:
            g1[tuple(i)] = 1 +g1.get(tuple(i),0)
        
        count = 0 
        g2 = {}  
        for col in range(len(grid)):
            r = []
            for row in range(len(grid)):
                r.append(grid[row][col])
            
            count += g1.get(tuple(r),0)
            #g2[tuple(r)] = 1 + g2.get(tuple(r),0)
        
        
        '''for i in g1.keys():
            if i in g2.keys():
                count += g1[i] * g2[i]'''
                
        return count