class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        def dfs(row,col,visited):
            visited.add((row,col))
            for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
                x = row + dx
                y = col + dy
                
                if 0 <= x < len(heights) and 0 <= y < len(heights[0]) and (x,y) not in visited and heights[row][col] <= heights[x][y]:
                    dfs(x,y,visited)
                    
        pacific = set()
        atlantic = set()
        for i in range(len(heights)):
            dfs(i,0,atlantic)
            dfs(i,len(heights[0])-1,pacific)
            
            
        for j in range(len(heights[0])):
            dfs(0,j,atlantic)
            dfs(len(heights)-1,j,pacific)
            
        
        print(pacific)
        print(atlantic)
        print(list(pacific & atlantic))
        return list(pacific & atlantic)