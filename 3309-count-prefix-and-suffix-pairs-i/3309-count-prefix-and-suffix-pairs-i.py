class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            w = len(words[i])
            for j in range(i+1,len(words)):
                if w > len(words[j]):
                    continue
                if words[j][:w] == words[i] and words[j][-w:] == words[i]:
                    count += 1
        return count

                
                
