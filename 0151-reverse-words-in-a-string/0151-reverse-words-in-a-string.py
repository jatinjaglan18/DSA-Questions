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
    