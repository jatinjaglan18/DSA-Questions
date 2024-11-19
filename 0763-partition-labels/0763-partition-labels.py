class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i,0)
        
        ans = []
        st = set()
        l,r=0,0
        while r<len(s):
            st.add(s[r])
            d[s[r]] -= 1
            if d[s[r]] == 0:
                st.remove(s[r])
            if len(st) == 0:
                ans.append(r-l+1)
                l = r+1
            r += 1
            
        return ans