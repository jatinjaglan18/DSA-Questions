class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [[0 for j in range(n)] for i in range(n)]
        result = []
            
        def printNqueens(board,row):
            if row == len(board):
                ans = []
                for i in board:
                    res = ''
                    for j in i:
                        if j == 0:
                            res+='.'
                        else:
                            res+='Q'
                    ans.append(res)
                result.append(ans)
                return
            
            for col in range(n):
                if is_queen_safe(board,row,col):
                    board[row][col] = 1
                    printNqueens(board,row+1)
                    board[row][col] = 0
                
                       
        
        def is_queen_safe(board,row,col):
            #vertical
            for i in range(row-1,-1,-1):
                if board[i][col] == 1:
                    return False
            
            #daigonal
            i = row-1
            j = col-1
            
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1
            
            #daigonal
            i = row-1
            j = col+1
            while i >= 0 and j < len(board[0]):
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1
                
            return True
    
        printNqueens(board,0)
        return result