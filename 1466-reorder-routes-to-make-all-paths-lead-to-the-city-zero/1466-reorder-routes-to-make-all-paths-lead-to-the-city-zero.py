class Solution:
    def __init__(self):
        self.res = 0
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
            
        edges = set()
        for i in connections:
            u = i[0]
            v = i[1]
            edges.add((u,v))
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [False for i in range(n)]
        self.tree(graph,0,edges,visited)
        return self.res   
    
    def tree(self,g,s,e,v):
        v[s] = True
        for i in range(len(g[s])):
            nbr = g[s][i]
            if v[nbr] == False:
                if (nbr,s) not in e:
                    self.res += 1
                self.tree(g,nbr,e,v)
        
                