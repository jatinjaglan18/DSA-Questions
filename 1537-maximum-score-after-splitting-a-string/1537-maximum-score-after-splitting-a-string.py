class Solution:
    def maxScore(self, s: str) -> int:
        left = ''
        right = ''
        ans = 0 
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            l = left.count('0')
            r=right.count('1')
            c = l+r
            ans = max(ans, c)
        return ans