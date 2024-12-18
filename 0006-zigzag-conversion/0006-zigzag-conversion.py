class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1 or numRows >= len(s):
            return s
        l = [[] for i in range(numRows)]
        idx = 0
        d = 1
        for i in s:
            l[idx].append(i)
            if idx == 0:
                d = 1
            elif idx == numRows-1:
                d = -1
            idx += d
            
        ans = ''
        for i in l:
            v = ''.join(i)
            ans += v
        
        return ans