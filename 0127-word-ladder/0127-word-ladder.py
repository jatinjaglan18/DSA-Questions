class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        graph = {}
        for word in wordList:
            for c in range(len(word)):
                k = word[:c] + '*' + word[c+1:]
                graph[k] = graph.get(k,[]) + [word]
        
        q = [beginWord]
        count = 1
        visit = set([beginWord])
        while q:
            for i in range(len(q)):
                
                word = q.pop(0)

                if word == endWord:
                    return count

                for c in range(len(word)):
                    k = word[:c] + '*' + word[c+1:]
                    for nbr in graph[k]:
                        if nbr not in visit:
                            visit.add(nbr)
                            q.append(nbr)
            
            count += 1
            
        return 0
            