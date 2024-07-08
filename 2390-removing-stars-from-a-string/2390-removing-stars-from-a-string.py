class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
           
        string = ''
        for i in stack:
            string += i
            
        return string