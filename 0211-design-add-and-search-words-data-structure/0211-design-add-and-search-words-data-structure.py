class Node:
    def __init__(self):
        self.children = {} #a : Node()
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.endofword = True

    def search(self, word: str) -> bool:
        
        def dfs(idx,root):
            cur = root
            for i in range(idx,len(word)):
                if word[i] =='.':
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            
            return cur.endofword
        
        return dfs(0,self.root)
                
        
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)