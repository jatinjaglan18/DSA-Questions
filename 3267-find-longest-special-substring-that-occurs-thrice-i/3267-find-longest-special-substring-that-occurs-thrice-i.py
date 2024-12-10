class Solution:
    def maximumLength(self, s: str) -> int:
        substring = []
        for i in range(len(s)):
            index = i
            while index < len(s) and s[i] == s[index]:
                substring.append(s[i:index+1])
                index +=1
        d = {}
        for i in (substring):
            d[i] = 1 + d.get(i,0)
        
        max_len = -1
        for i in d.keys():
            if d[i] >= 3 and len(i) > max_len:
                max_len = len(i)
        return max_len