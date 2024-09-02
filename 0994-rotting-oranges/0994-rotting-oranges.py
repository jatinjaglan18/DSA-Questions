class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
         
        count = 0
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j,0])       #r,c,t
                if grid[i][j] == 1:
                    count += 1
                
        if count == 0:
            return 0
        if not q:
            return -1
        
        time = -1
        '''while q:
            size = len(q)
            while size :
                val = q.popleft()
                r = val[0]
                c = val[1]
                size -= 1

                for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        count -= 1'''
        while q:
            val = q.popleft()
            r = val[0]
            c = val[1]
            t = val[2]
            time = t
            
            
            
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append([nr,nc,t+1])
                    count -= 1
            
                    
        if count != 0:
            return -1
        return time
                    
                    
                    