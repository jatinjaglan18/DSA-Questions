class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d_c = {}
        d_b = {}
        ans  = []
        for b,c in queries:

            prev_color = d_b.get(b,None)
            if prev_color:
                d_c[prev_color].pop()
                if len(d_c[prev_color]) == 0:
                    d_c.pop(prev_color)

            d_c[c] = d_c.get(c,[]) + [b]
            d_b[b] = c
            
            ans.append(len(d_c))
        return ans

        