def operations(v1,v2,o):
    if o == '+':
        v = v1 + v2
    elif o == '-':
        v = v2 - v1
    elif o == '*':
        v = v2 * v1
    elif o == '/':
        v = int(v2 / v1)
    return v
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = []
        
        for i in tokens:
            if i in '+,-,/,*':
                v1 = opr.pop()
                v2 = opr.pop()
                
                v = operations(v1,v2,i)
                
                opr.append(v)
            else:
                opr.append(int(i))
                
        return int(opr[-1])
                