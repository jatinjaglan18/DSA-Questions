class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        freq = {}
        for i in s:
            freq[i]=1+freq.get(i,0)
        count = 0
        for i in freq.keys():
            if freq[i] % 2 != 0:
                count += 1
        return count <= k
        