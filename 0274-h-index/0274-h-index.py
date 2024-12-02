class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0] * (n+1)

        for i,v in enumerate(citations):
            if v > n:
                temp[n] += 1
            else:
                temp[v] += 1
        s = 0
        for i in range(n, -1, -1):
            s += temp[i]
            if s >= i:
                return i
        return 0
            