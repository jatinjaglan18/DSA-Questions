class Node:
    def __init__(self):
        self.children = {}
        self.endofword = False
    
    def addword(self, word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.endofword = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Prefix Trie
        root = Node()
        for w in words:
            root.addword(w)
            
        row = len(board)
        col = len(board[0])
        visited = [[0 for j in range(col)] for i in range(row)]    
        res = set()
        
        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r == row or c == col or visited[r][c] == 1 or board[r][c] not in node.children:
                return
            
            visited[r][c] = 1
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endofword:
                res.add(word)
                
            dfs(r,c+1,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r-1,c,node,word)
            
            visited[r][c] = 0
            
            
        for i in range(row):
            for j in range(col):
                dfs(i,j,root,'')
                
        return list(res)
                
            
        
        