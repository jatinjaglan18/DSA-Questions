class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) == 3:
            if s[0] != s[-1]:
                return 0
            else:
                return 1
        ans = 0
        S = set(s)
        for cs in S:
            i = 0
            j = 0
            for ci in range(len(s)):
                if cs == s[ci]:
                    i = ci
                    break
            for ci in range(len(s)-1,-1,-1):
                if s[ci] == cs:
                    j = ci
                    break
            if j - i > 1:
                ans += len(set(s[i+1:j]))
        
        return ans


        


        