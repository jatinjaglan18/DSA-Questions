class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row = len(board)
        col = len(board[0])
        
        visited = [[0 for j in range(col)] for i in range(row)]
        res = ''
        
        def backtrack(r,c,idx):
            #base
            
            if idx == len(word):
                return True
            
            if r < 0 or r == row or c < 0 or c == col or visited[r][c] == 1 or board[r][c] != word[idx]:
                return False
            
            
            visited[r][c] = 1
            
            r_c1 = backtrack(r,c+1,idx+1)
            r1_c = backtrack(r+1,c,idx+1)
            r_c_1 = backtrack(r,c-1,idx+1)
            r_1_c = backtrack(r-1,c,idx+1)
                
            if r_c1 or r1_c or r_c_1 or r_1_c:
                return True
        
            visited[r][c] = 0
            
            return False
    
            
            
        for i in range(row):
            for j in range(col):
                
                if backtrack(i,j,0):
                    return True
                
        return False
        