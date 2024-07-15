class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        string = set()
        l , r = 0,0
        max_len = 0
        while r < len(s):
            while s[r] in string:
                string.remove(s[l])
                l += 1
            string.add(s[r])
            if max_len < len(string):
                max_len = len(string)
            r += 1
        return max_len
            
        
        
            
        