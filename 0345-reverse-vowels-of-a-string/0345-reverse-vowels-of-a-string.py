class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        '''v_l = []
        for i in range(len(s)):
            if s[i] in vowels:
                v_l.append(s[i])
                s = s[:i] + '$' + s[i+1:]
                
        j = len(v_l) - 1
        for i in range(len(s)):
            if s[i] == '$':
                s = s[:i] + v_l[j] + s[i+1:]
                j -= 1
                
        return s'''
                
        l = 0
        r = len(s)-1
        string = s
        while l < r:
            if s[l] not in vowels:
                l += 1
                
            if s[r] not in vowels:
                r -= 1
            
            if l != r and s[l] in vowels and s[r] in vowels:
                string = string[:l] + s[r] +string[l+1:r] + s[l] +string[r+1:]
                l += 1
                r -= 1
                  
        return string
    
    