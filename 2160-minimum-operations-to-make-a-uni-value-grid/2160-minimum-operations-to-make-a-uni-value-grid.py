class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = [j for i in grid for j in i]
        l.sort()

        diff = [abs(val - l[0]) % x for val in l]
        if any(d != 0 for d in diff):
            return -1
        
        median = l[len(l)//2]
        opr = sum(abs(val-median)// x for val in l)
        return opr