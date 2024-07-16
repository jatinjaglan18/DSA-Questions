class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = {}
        col = {}
        box = {}
        for i in range(9):
            row[i] = set()
            col[i] = set()
            for j in range(9):
                box[(i//3,j//3)] = set()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in box[(r//3,c//3)]:
                    return False
                
                
                row[r].add(board[r][c])
                    
                
                col[c].add(board[r][c])
                    
                
                box[(r//3,c//3)].add(board[r][c])
                    
        return True
                
                    