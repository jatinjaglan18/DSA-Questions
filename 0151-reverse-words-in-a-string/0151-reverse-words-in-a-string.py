class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        s = ' '.join(s)
        return s
        '''str = ''
        for i in s:
            str = str + i + ' '
        return str[:len(str)-1]'''
        
        '''#using stack
        stack = []
        string = ''
        for i in s:
            
            if i == ' ':
                while len(stack) != 0:
                    string = stack.pop() + string
                
                if len(string) != 0 and string[0] != ' ':
                    string = ' ' + string
                
            else:
                stack.append(i)
                
        while len(stack) != 0 :
            string = stack.pop() + string
        
        while string[0] == ' ':
            string = string[1:]
        while string[len(string) -1] == ' ':
            string = string[:len(string) -1]
        return string'''