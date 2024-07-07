class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        elif set(word1) != set(word2):
            
            return False
        
        else:
            w1 = {}
            w2 = {}
            for i in range(len(word1)):
                w1[word1[i]] = 1 + w1.get(word1[i],0)
                w2[word2[i]] = 1 + w2.get(word2[i],0)
            
            
            if sorted(w1.values()) == sorted(w2.values()):
                return True
            
            else:
                return False