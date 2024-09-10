class Trie:

    def __init__(self):
        self.prefixes = set()
        self.words = set()

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.prefixes.add(word[:i+1])
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixes:
            return True
        else:
            return False
            
                    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)