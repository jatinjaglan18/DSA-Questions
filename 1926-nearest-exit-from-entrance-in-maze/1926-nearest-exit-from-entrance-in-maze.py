class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        '''#visited = [[False for i in range(len(maze[0]))] for i in range(len(maze))]
        
        res = float('inf')
        
        q = deque()
        q.append([entrance[0],entrance[1],0])
        
        while q:
            
            val = q.popleft()
            
            r = val[0]
            c = val[1]
            l = val[2]
            maze[r][c] = '+'
            
            if [r,c] != entrance:
                if r == 0 or c == 0 or r == len(maze) - 1 or c == len(maze[0]) - 1:
                    res = l
                    return res            
                    
            
            #North
            if r - 1 >= 0 and maze[r-1][c] == '.':
                q.append([r-1,c,l+1])
            #East
            if c + 1 < len(maze[0]) and maze[r][c+1] == '.':
                q.append([r,c+1,l+1])
                
            #South
            if r+1 < len(maze) and maze[r+1][c] == '.':
                q.append([r+1,c,l+1])
            
            #West
            if c - 1 >= 0 and maze[r][c-1] == '.':
                q.append([r,c-1,l+1])
                
            
        return -1'''
        
        m = len(maze)
        n = len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)]) # step 1
        maze[entrance[0]][entrance[1]] = "+" # step 2

        while queue:
            row, col, steps = queue.popleft() # step 3

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # step 4
                nr, nc = row + dy, col + dx
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".": # step 5
                    if (nr == 0 or nr == m - 1) or (nc == 0 or nc == n - 1):
                        return steps + 1

                    maze[nr][nc] = "+"
                    queue.append((nr, nc, steps + 1))

        return -1 # step 6
            
            