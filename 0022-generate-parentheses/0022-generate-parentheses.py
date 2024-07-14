
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []
        self.parent('',0,0)
        return self.result
    
    def parent(self,s, ob, cb):
        if len(s) == 2*self.n:
            self.result.append(s)
            return
        if ob < self.n:
            self.parent(s+'(', ob+1, cb)
        if cb < ob:
            self.parent(s+')', ob, cb + 1)
        