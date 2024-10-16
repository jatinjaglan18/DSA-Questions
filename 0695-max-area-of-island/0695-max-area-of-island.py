class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))] 
        return self.island(grid,visited)
        
    def island(self,m,v):
        max_area = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 1 and v[i][j] == False:
                    area = self.tree(m,i,j,v)
                    if area > max_area:
                        max_area = area
        return max_area
    
    def tree(self,m,i,j,v):
        if i < 0 or j < 0 or i == len(m) or j == len(m[0]) or m[i][j] == 0 or v[i][j] == True:
            return 0
        
        v[i][j] = True
        a = 1
        a += self.tree(m,i+1,j,v)
        a += self.tree(m,i,j+1,v)
        a += self.tree(m,i-1,j,v)
        a += self.tree(m,i,j-1,v)
        
        return a
        
        
                    
        
        
        
        
        