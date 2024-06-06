class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s={}
        d_t={}
        
        for i in s:
            if i in d_s.keys():
                d_s[i] += 1
                
            else:
                d_s[i] = 1
                
        for j in t:
            if j in d_t.keys():
                d_t[j] += 1
            else:
                d_t[j] = 1
        
        m = d_s
        if len(d_t) > len(d_s):
            m = d_t
        
        for key in m.keys():
            if d_t.get(key) != d_s.get(key):
                
                return False
                break
        else:
            return True
            
        