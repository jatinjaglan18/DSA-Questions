class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        v_l = []
        for i in range(len(s)):
            if s[i] in vowels:
                v_l.append(s[i])
                s = s[:i] + '$' + s[i+1:]
                
        j = len(v_l) - 1
        for i in range(len(s)):
            if s[i] == '$':
                s = s[:i] + v_l[j] + s[i+1:]
                j -= 1
                
        return s
                
        '''string1 = ''
        string2 = ''
        l = 0
        r = len(s)-1
        
        while l < r:
            if s[l] not in vowels:
                string1 = string1 + s[l]
                l += 1
                
            elif s[r] not in vowels:
                string2 = s[r] + string2
                r -= 1
            
            else:
                string1 = string1 + s[r]
                string2 = s[l] + string2
                l += 1
                r -= 1
                
        string = string1 + string2   
        return string'''