class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.split()
        s.reverse()
        str = ''
        for i in s:
            str = str + i + ' '
        return str[:len(str)-1]