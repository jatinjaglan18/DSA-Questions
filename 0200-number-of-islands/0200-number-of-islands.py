class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        
        return self.count_islands(grid,visited)
        
    def count_islands(self,m,v):
        count = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == '1' and v[i][j] == False:
                    self.tree(m,i,j,v)
                    count+=1
        return count
        
    def tree(self,m,i,j,v):
        
        if i < 0 or j < 0 or i == len(m) or j == len(m[0]) or v[i][j] == True or m[i][j] == '0':
            return
        
        v[i][j] = True
        self.tree(m,i+1,j,v)
        self.tree(m,i,j+1,v)
        self.tree(m,i-1,j,v)
        self.tree(m,i,j-1,v)
        
        
        