class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        res = ''
        s = s.lstrip()
        if s == '':
            return 0
        if len(s) == 1 and not s[0].isdigit():
           return 0
        if s[0] == '-' or s[0] == '+':
            sign = 1
        elif not s[0].isdigit():
            return 0
        else:
            res += s[0]
        for i in range(1,len(s)):
            if s[i].isdigit():
                res+=s[i]
            else:
                break
        if sign:
            res=s[0] + res
        try:
            ans = (int(res))
        except:
            return 0
        
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 -1:
            return 2**31 - 1
        else:
            return ans