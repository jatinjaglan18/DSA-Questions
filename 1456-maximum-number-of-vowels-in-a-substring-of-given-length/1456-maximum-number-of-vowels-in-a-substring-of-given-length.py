class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        num_vol = 0
        for i in s[:k]:
            if i in 'aeiou':
                num_vol += 1
        max_vol = num_vol
        
        for i in range(k,len(s)):
            if s[i] in 'aeiou' :
                num_vol += 1
            if s[i-k] in 'aeiou' :
                num_vol -= 1
                
            if max_vol < num_vol:
                max_vol = num_vol
            
        return max_vol
            