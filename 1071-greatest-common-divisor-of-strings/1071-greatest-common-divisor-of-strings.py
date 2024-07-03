class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        if str1 == str2:
            return str1
        
        if len(str1) > len(str2):
            l = str1
            s = str2
        else:
            l = str2
            s = str1
            
        return self.gcdOfStrings(l[len(s):],s)

            