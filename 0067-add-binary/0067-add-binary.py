class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        
        ia = len(a)-1
        ib = len(b)-1
        
        while ia >= 0 or ib >= 0 or carry == 1:
            if ia >= 0:
                carry += int(a[ia])
                ia -= 1
            if ib >= 0:
                carry += int(b[ib])
                ib -= 1
            res.append(str(carry % 2))
            carry = carry // 2
        
        return ''.join(res[::-1])
                