class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        
        memo = {}
        
        def dfs(r,c,preval):
            if r < 0 or r == row or c < 0 or c == col or matrix[r][c] <= preval:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            ans = 1
            
            ans = max(ans, 1 + dfs(r+1,c,matrix[r][c]))
            ans = max(ans, 1 + dfs(r-1,c,matrix[r][c]))
            ans = max(ans, 1 + dfs(r,c+1,matrix[r][c]))
            ans = max(ans, 1 + dfs(r,c-1,matrix[r][c]))
            
            memo[(r,c)] = ans
            return ans
        
        for r in range(row):
            for c in range(col):
                dfs(r,c,-1)
        return max(memo.values())