class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        max_len = 0
        m_f = 0
        for i in range(len(s)):
            d[s[i]] = 1 + d.get(s[i],0)
            m_f = max(m_f,d[s[i]])
            while (i - l + 1) - m_f > k:
                d[s[l]] -= 1
                l += 1
                
            max_len = max(i - l + 1, max_len)
        return max_len
            
                
                