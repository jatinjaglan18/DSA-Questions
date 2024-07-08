class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        
        for i in s:
            s_t = ''
            if i == ']':
                while stack[-1] != '[':
                    v = stack.pop()
                    s_t = v + s_t
                stack.pop()
                m = ''
                while len(stack) != 0 and stack[-1] in '0123456789':
                    val = stack.pop()
                    m = val + m
                res = s_t * int(m)
                stack.append(res)
            else:
                stack.append(i)
               
        res = ''
        while len(stack) != 0:
            v = stack.pop()
            res = v + res
            
        return res