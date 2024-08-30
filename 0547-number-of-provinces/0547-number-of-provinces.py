class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for i in range(len(isConnected))]
        count = 0
        for i in range(len(isConnected)):
            if visited[i] == False:
                self.tree(isConnected,i,visited)
                count+= 1
        return count
        
    
    def tree(self,mat,s,v):
        
        v[s] = True
        for i in range(len(mat)):
            if mat[s][i] == 1 and v[i] == False:
                self.tree(mat,i,v)
                