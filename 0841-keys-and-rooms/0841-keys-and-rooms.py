class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in range(len(rooms))]
        comps = []
        for i in range(len(rooms)):
            if visited[i] == False:
                comp = []
                self.tree(rooms,i,visited,comp)
                comps.append(comp)
                if len(comps) > 1:
                    return False
        else:
            return True
        
    def tree(self,graph,src,v,c):
        c.append(src)
        v[src] = True
        for i in range(len(graph[src])):
            nbr = graph[src][i]
            if v[nbr] == False:
                self.tree(graph,nbr,v,c)
                
                    
                    