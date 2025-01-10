class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = []
        
        w2_count={}
        for w2 in words2:
            for w in w2:
                c = w2.count(w)
                if w not in w2_count or c > w2_count[w]:
                    w2_count[w] = c

        print(w2_count)
            
        for w in words1:
            for i in w2_count:
                if w.count(i) < w2_count[i]:
                    break
            else:
                res.append(w)
        return res


        