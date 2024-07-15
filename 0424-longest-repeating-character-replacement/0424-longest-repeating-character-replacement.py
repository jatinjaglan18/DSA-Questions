class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        max_len = 0
        for i in range(len(s)):
            d[s[i]] = 1 + d.get(s[i],0)
            
            while (i - l + 1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
                
            max_len = max(i - l + 1, max_len)
        return max_len
                
                