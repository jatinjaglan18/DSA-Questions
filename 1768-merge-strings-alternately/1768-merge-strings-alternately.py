class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        #w2 = 0
        s = ''
        while w1 < len(word1) and w1 < len(word2):
            s = s + word1[w1] + word2[w1] 
            w1 += 1
            
        while w1 < len(word1):
            s = s + word1[w1]
            w1 += 1
        
        while w1 < len(word2):
            s = s + word2[w1]
            w1 += 1
        
        return s