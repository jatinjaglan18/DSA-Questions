class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = len(needle)-1
        
        while j < len(haystack):
            temp = haystack[i:j+1]
            if temp == needle:
                return i
            i += 1
            j += 1
        return -1