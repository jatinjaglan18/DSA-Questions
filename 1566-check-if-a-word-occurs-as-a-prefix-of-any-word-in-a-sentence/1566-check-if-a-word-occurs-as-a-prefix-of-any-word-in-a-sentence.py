class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent = sentence.split()
        l = len(searchWord)
        for i in range(len(sent)):
            if sent[i][:l] == searchWord:
                return i + 1
        return -1