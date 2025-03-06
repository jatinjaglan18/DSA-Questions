class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        s = set()
        for i in grid:
            for j in i:
                if j in s:
                    ans.append(j)
                s.add(j)

        n = len(grid)
        m = n * n
        t_s = (m*(m+1))//2
        ans.append(t_s - sum(s))
        return ans
        