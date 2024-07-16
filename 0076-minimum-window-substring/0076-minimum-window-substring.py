class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapt = {}
        maps = {}
        
        for i in t:
            mapt[i] = 1 + mapt.get(i,0)
            maps[i] = 0
        l = 0
        r = 0
        min_len = 10**5
        ans = ''
        have = 0
        need = len(mapt)
        for r in range(len(s)):
            if s[r] in mapt.keys():
                maps[s[r]] += 1
            
            if s[r] in mapt.keys() and maps[s[r]] == mapt[s[r]]:
                have += 1
                
            while have == need:
                length = len(s[l:r+1])
                if length < min_len:
                    min_len = length
                    ans = s[l:r+1]
                
                if s[l] in maps.keys():
                    maps[s[l]] -= 1
                    if maps[s[l]] < mapt[s[l]]:
                        have -= 1
                
                l += 1
                
        if min_len == 10**5:
            return ''
        else:
            return ans
            
            
        
        
        
        