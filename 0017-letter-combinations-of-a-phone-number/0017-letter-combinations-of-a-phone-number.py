class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        print(len(digits))
        string = ['', '','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        if len(digits) == 0:
            return []
        
        ch = digits[0]
        r = self.letterCombinations(digits[1:])
        res = []
        for i in string[int(ch)]:
            if len(r) == 0:
                res.append(i)
            else:
                for j in r:
                    res.append(i+j)

        return res