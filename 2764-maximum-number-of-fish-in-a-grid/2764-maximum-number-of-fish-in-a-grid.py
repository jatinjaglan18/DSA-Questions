class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        water = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    water.append((i,j))
        ans = 0
        visited = set()
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            fish = 0
            visited.add((i,j))
            fish += grid[i][j]
            for di,dj in dir:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0 and (ni,nj) not in visited:
                    fish += dfs(ni,nj)
            return fish
        for i,j in water:
            if (i,j) not in visited:
                ans = max(ans,dfs(i,j))
        return ans
        