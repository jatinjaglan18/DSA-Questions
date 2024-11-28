class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        src = (0,0)
        des = (len(grid) - 1, len(grid) - 1)
        
        heap = [(grid[0][0], 0,0)]
        visit = set()
        
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap:
            t, sr, sc = heapq.heappop(heap)
            if (sr,sc) == des:
                return t
            
            for dr,dc in moves:
                if sr + dr < 0 or sr + dr == len(grid) or sc + dc < 0 or sc + dc == len(grid) or (sr + dr, sc + dc) in visit:
                    continue
                visit.add((sr+dr, sc+dc))
                
                heapq.heappush(heap, (max(t, grid[sr+dr][sc+dc]), sr+dr, sc+dc))
            
            